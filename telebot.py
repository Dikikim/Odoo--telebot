import telegram
import odoo

bot = telegram.Bot('6071402460:AAGwpvtpBb18j2hjVIKuEFauhABpLVm7-oE')

odoo_db = odoo.Odoo('http://192.168.0.103:8069', 'odoo16', 'odoo', '1990')

# Define a function to handle incoming messages
def handle_message(update, context):
    chat_id = update.message.chat_id
    message_text = update.message.text

    # Get the sales information from Odoo based on the phone number provided in the message
    sales_info = odoo_db.get_sales_info(message_text)

    # Create a message to send back to the user
    response = f"Sales info for {message_text}:\n"
    response += f"Number: {sales_info['number']}\n"
    response += f"Creation date: {sales_info['creation_date']}\n"
    response += f"Customer: {sales_info['customer']}\n"
    response += f"Salesperson: {sales_info['salesperson']}\n"
    response += f"Activities: {sales_info['activities']}\n"
    response += f"Total: {sales_info['total']}\n"
    response += f"Status: {sales_info['status']}\n"
    response += f"Total monthly sales: {sales_info['total_monthly_sales']}"

    # Send the message back to the user
    bot.send_message(chat_id=chat_id, text=response)

# Set up the updater and dispatcher to handle incoming messages
updater = telegram.Updater('6071402460:AAGwpvtpBb18j2hjVIKuEFauhABpLVm7-oE', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.MessageHandler(telegram.Filters.text, handle_message))

updater.start_polling()


# import telegram
# from odoo import models, fields, api
#
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#     number = fields.Char()
#     creation_date = fields.Date()
#     customer = fields.Char()
#     salesperson = fields.Char()
#     activities = fields.Char()
#     total = fields.Float()
#     status = fields.Char()
#
#     @api.model
#     def get_sales_info(self, phone_number):
#         # logic to query Odoo DB and format sales information based on the phone number provided
#         sales_info_dict = {}
#         sale_orders = self.search([('partner_id.phone', '=', phone_number)])
#         for order in sale_orders:
#             sales_info_dict[order.number] = {'creation_date': order.creation_date,
#                                              'customer': order.customer,
#                                              'salesperson': order.salesperson,
#                                              'activities': order.activities,
#                                              'total': order.total,
#                                              'status': order.status}
#         return sales_info_dict
#
#     @api.model
#     def get_total_monthly_sales(self):
#         # logic to calculate and return total monthly sales
#         return total_monthly_sales
#
# def start_bot():
#     api_token = '6071402460:AAGwpvtpBb18j2hjVIKuEFauhABpLVm7-oE'
#     updater = telegram.ext.Updater(api_token, use_context=True)
#     dispatcher = updater.dispatcher
#     dispatcher.add_handler(telegram.ext.CommandHandler('sales', get_sales_info_handler))
#     dispatcher.add_handler(telegram.ext.CommandHandler('monthly_sales', get_monthly_sales_info_handler))
#     updater.start_polling()
#
# def get_sales_info_handler(update, context):
#     # retrieve phone number argument from command
#     args = context.args
#     if len(args) != 1:
#         update.message.reply_text('Please provide a phone number.')
#         return
#     phone_number = args[0]
#     # retrieve and format sales information
#     sales_info_dict = SaleOrder.get_sales_info(phone_number)
#     if sales_info_dict:
#         sales_info_string = 'Sales Information for Phone Number {}:'.format(phone_number)
#         for order_number, order_info in sales_info_dict.items():
#             sales_info_string += '\n\nOrder Number: {}\nCreation Date: {}\nCustomer: {}\nSalesperson: {}\nActivities: {}\nTotal: {}\nStatus: {}'.format(order_number,
#                                                                                                                                                    order_info['creation_date'],
#                                                                                                                                                    order_info['customer'],
#                                                                                                                                                    order_info['salesperson'],
#                                                                                                                                                    order_info['activities'],
#                                                                                                                                                    order_info['total'],
#                                                                                                                                                    order_info['status'])
#         update.message.reply_text(sales_info_string)
#     else:
#         update.message.reply_text('No sales found for phone number {}.'.format(phone_number))
#
# def get_monthly_sales_info_handler(update, context):
#     # retrieve and format total monthly sales information
#     total_monthly_sales = SaleOrder.get_total_monthly_sales()
#     monthly_sales_info_string = 'Total Monthly Sales: {}'.format(total_monthly_sales)
#     update.message.reply_text(monthly_sales_info_string)
#
# if __name__ == '__main__':
#     start_bot()
