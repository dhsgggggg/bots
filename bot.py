from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace YOUR_BOT_TOKEN with your actual bot token
updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

def time(update, context):
    import datetime
    now = datetime.datetime.now()
    update.message.reply_text('The current time is {}'.format(now))

time_handler = MessageHandler(Filters.regex(r'(\btime\b|\bوقت\b)'), time)
dispatcher.add_handler(time_handler)

updater.start_polling()
updater.idle()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace YOUR_BOT_TOKEN with your actual bot token
updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

def time(update, context):
    import datetime
    now = datetime.datetime.now()
    update.message.reply_text('The current time is {}'.format(now))

time_handler = MessageHandler(Filters.regex(r'(\btime\b|\bوقت\b)'), time)
dispatcher.add_handler(time_handler)

def start(update, context):
    update.message.reply_text('Bot started')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def error(update, context):
    print(f"Update {update} caused error {context.error}")
    update.message.reply_text("Sorry, I couldn't process your message. Please try again later.")

dispatcher.add_error_handler(error)

updater.start_polling()
updater.idle()
