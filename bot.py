from telegram.ext import Updater, CommandHandler

# Replace YOUR_BOT_TOKEN with your actual bot token
updater = Updater(token='5707101777:AAH2ttEJTJCv0YcnATqsY_zrsD0IdSNd5e4', use_context=True)

def time(update, context):
    import datetime
    now = datetime.datetime.now()
    update.message.reply_text('The current time is {}'.format(now))

time_handler = CommandHandler('time', time)
dispatcher.add_handler(time_handler)

updater.start_polling()
updater.idle()
