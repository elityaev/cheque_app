from datetime import datetime

from sqlalchemy import select


# from db.category import get_sub_category
from .bot_db_models import Receipt, session, Product


def get_receipt_data(receipt_data):
    receipt_dict = {}
    receipt_dict['date'] = datetime.strptime(receipt_data['operation']['date'], "%Y-%m-%dT%H:%M")
    receipt_dict['organization'] = receipt_data['organization']['name']
    receipt_dict['total_sum'] = receipt_data['operation']['sum'] / 100
    if "'" in receipt_dict['organization']:
        receipt_dict['organization'] = receipt_dict['organization'].replace("'", " ")
    return receipt_dict


def save_receipt(receipt_dict):
    receipt = Receipt(
        date=receipt_dict['date'],
        organization=receipt_dict['organization'],
        summa=receipt_dict['total_sum']
    )
    session.add(receipt)
    session.commit()
    return receipt


def get_product_data(product_data):
    product_list = []
    items = product_data['ticket']['document']['receipt']['items']
    for item in items:
        product_dict = {}
        product_dict['name'] = item['name'].lstrip('1234567890:*.^- ')
        if '"' in product_dict['name']:
            product_dict['name'] = product_dict['name'].replace('"', '')
        product_dict['price'] = item['price'] / 100
        product_dict['quantity'] = item['quantity']
        product_dict['summa'] = item['sum'] / 100
        product_list.append(product_dict)
    return product_list


def save_products(product_list, receipt):
    for i in range(len(product_list)):
        product = Product(
            name=product_list[i]['name'],
            quantity=product_list[i]['quantity'],
            price=product_list[i]['price'],
            sum=product_list[i]['summa'],
            receipt_id=receipt.id,
        )
        session.add(product)
        session.commit()



# def save_check(check_data):
#     data_dict = {}
#     data_dict['date'] = datetime.strptime(check_data['operation']['date'], "%Y-%m-%dT%H:%M")
#     data_dict['organization'] = check_data['organization']['name']
#     data_dict['total_sum'] = check_data['operation']['sum'] / 100
#     if "'" in data_dict['organization']:
#         data_dict['organization'] = data_dict['organization'].replace("'", " ")
#     check = Check(
#         date=data_dict['date'],
#         organization=data_dict['organization'],
#         summa=data_dict['total_sum']
#     )
#     session.add(check)
#     session.commit()
#     return check


# def save_product(check_data, check):
#     data_dict = {}
#     items = check_data['ticket']['document']['receipt']['items']
#     for item in items:
#         data_dict['name'] = item['name'].lstrip('1234567890:*.^- ')
#         if '"' in data_dict['name']:
#             data_dict['name'] = data_dict['name'].replace('"', '')
#         data_dict['price'] = item['price']/100
#         data_dict['quantity'] = item['quantity']
#         data_dict['summa'] = item['sum'] / 100
#         sub_category = get_sub_category(data_dict['name'])
#         product = Product(
#             name=data_dict['name'],
#             quantity=data_dict['quantity'],
#             price=data_dict['price'],
#             sum=data_dict['summa'],
#             check_id=check.id,
#             sub_category_id=sub_category
#         )
#         session.add(product)
#         session.commit()
#     products_in_check = session.execute(select(Product).where(Product.check_id == check.id))
#     products_in_check = products_in_check.scalars().all()
#     return products_in_check
#
# def processing_check(data):
#     check_data = get_check(data)
#     check = save_check(check_data)
#     products = save_product(check_data, check)
#     return check, products