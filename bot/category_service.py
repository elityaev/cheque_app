from sqlalchemy import select

from .bot_db_models import session, Product, SubCategory, Category


def get_product_name(product_name):
    product = session.execute(select(Product).where(Product.name == product_name))
    product = product.scalars().first()
    return product

# def get_sub_category(value):
#     product = session.execute(select(Product).where(Product.name == value))
#     product = product.scalars().first()
#     if product:
#         sub_category_id = session.execute(select(product.sub_category_id))
#         sub_category_id = sub_category_id.scalars().first()
#         if sub_category_id:
#             return sub_category_id
#     category_list = session.execute(select(Category.id, Category.name)).all()
#     category_id = request_for_selection_category(update, value, category_list)
#     for category in category_list:
#         print(category)
#     category_id = input(
#         f'Введите номер категории, к которой нужно отнести новую продукцию {value}:\n'
#     )
#     sub_category_list = session.execute(select(
#         SubCategory.id, SubCategory.name
#     ). where(SubCategory.category_id == category_id)).all()
#     sub_category_id = input(
#         f'Введите номер подкатегории, к которой нужно отнести новую продукцию {value}: '
#         f'{sub_category_list}. Если подходящей подкатегории нет, в ведите "n"'
#     )
#     if sub_category_id.isdigit():
#         return sub_category_id
#     sub_category_name = input(
#             f'Введите для продукции "{value}" название новой подкатегории: '
#         )
#     sub_category = SubCategory(name=sub_category_name, category_id=category_id)
#     session.add(sub_category)
#     session.commit()
#     print(sub_category.id)
#     return sub_category.id




    #
    # get_row_products = f'''
    #     SELECT * FROM transactions WHERE product="{value}"
    # '''
    # row = execute_read_query(connection, get_row_products)
    # if row:
    #     category_id = row[0][7]
    #     sub_category_id = row[0][8]
    #     return sub_category_id, category_id
    # else:
    #     sub_category = input(
    #         f'Введите для продукции "{value}" название новой подкатегории: '
    #     )
    #     get_sub_category = f'''
    #         SELECT * FROM sub_categories WHERE name="{sub_category}"
    #     '''
    #     row = execute_read_query(connection, get_sub_category)
    #     if row:
    #         sub_category_id, sub_category_name, category_id = row[0]
    #         return sub_category_id, category_id
    #     else:
    #         category = input(
    #             f'Введите для подкатегории "{sub_category}" название категории: '
    #         )
    #         get_category = f'''
    #             SELECT * FROM categories WHERE name="{category}"
    #         '''
    #         row = execute_read_query(connection, get_category)
    #         if row:
    #             category_id = row[0][0]
    #             create_sub_category = f'''
    #                     INSERT INTO
    #                         sub_categories (name, category_id)
    #                     VALUES
    #                         ("{sub_category}", {category_id})
    #                     '''
    #             execute_query(connection, create_sub_category)
    #             get_row_sub_categories = f'''
    #                 SELECT * FROM sub_categories WHERE name="{sub_category}"
    #             '''
    #             row = execute_read_query(connection, get_row_sub_categories)
    #             sub_category_id = row[0][0]
    #             return sub_category_id, category_id
    #         else:
    #             create_category = f'''
    #                     INSERT INTO
    #                         categories (name)
    #                     VALUES
    #                         ("{category}")
    #                     '''
    #             execute_query(connection, create_category)
    #             get_row_categories = f'''
    #                 SELECT * FROM categories WHERE name="{category}"
    #             '''
    #             row = execute_read_query(connection, get_row_categories)
    #             category_id, category_name = row[0]
    #             create_sub_category = f'''
    #                                 INSERT INTO
    #                                     sub_categories (name, category_id)
    #                                 VALUES
    #                                     ("{sub_category}", {category_id})
    #                                 '''
    #             execute_query(connection, create_sub_category)
    #             get_row_sub_categories = f'''
    #                 SELECT * FROM sub_categories WHERE name="{sub_category}"
    #             '''
    #             row = execute_read_query(connection, get_row_sub_categories)
    #             sub_category_id, sub_category_name, category_id = row[0]
    #             return sub_category_id, category_id