import logging
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def remove_russian_names(update: Update, context: CallbackContext):
    # Use context.args to access any additional arguments passed to the handler
    # ...

def main():
    updater = Updater("23818072")
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, remove_russian_names, pass_job_queue=True, pass_chat_data=True, database=db))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
