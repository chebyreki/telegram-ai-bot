from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

TOKEN = "8238824148:AAExDYUQiv1bKzDCpZ2OFQc9-yDZ-7j5nkg"

def start(update, context):
    update.message.reply_text("🤖 Бот работает 24/7!")

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()
updater.idle()
