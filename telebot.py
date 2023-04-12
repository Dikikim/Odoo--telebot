import telegram
import odoo

bot = telegram.Bot('api')

odoo_db = odoo.Odoo('http://', 'db_name', 'user_name', 'password')

def handle_message(update, context):
    chat_id = update.message.chat_id
    message_text = update.message.text

    sales_info = odoo_db.get_sales_info(message_text)

    response = f"Sales info for {message_text}:\n"
    response += f"Number: {sales_info['number']}\n"
    response += f"Creation date: {sales_info['creation_date']}\n"
    response += f"Customer: {sales_info['customer']}\n"
    response += f"Salesperson: {sales_info['salesperson']}\n"
    response += f"Activities: {sales_info['activities']}\n"
    response += f"Total: {sales_info['total']}\n"
    response += f"Status: {sales_info['status']}\n"
    response += f"Total monthly sales: {sales_info['total_monthly_sales']}"

    bot.send_message(chat_id=chat_id, text=response)

updater = telegram.Updater('api', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.MessageHandler(telegram.Filters.text, handle_message))

updater.start_polling()
