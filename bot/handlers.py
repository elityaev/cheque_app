from .ticket_service import get_receipt
from .processing import get_receipt_data, get_product_data, save_receipt, save_products


async def decode_qr_handler(update, context):
    data = update.message.text
    cheque_data = get_receipt(data)
    cheque_dict = get_receipt_data(cheque_data)
    cheque = save_receipt(cheque_dict)
    product_list = get_product_data(cheque_data)
    save_products(product_list, cheque)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Готово!")