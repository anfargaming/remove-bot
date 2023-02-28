import os
import logging
from telegram.ext import Updater, MessageHandler, Filters
from bot import remove_russian_names
from database import Database

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Get MongoDB URL from environment variable
MONGO_URL = os.environ.get('MONGODB_URL')

# Initialize database
db = Database(MONGO_URL, "Cluster0")

def main():
    """Start the Telegram bot."""
    # Create the Telegram bot
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add message handler to remove users with Russian alphabet in their names
    dp.add_handler(MessageHandler(Filters.text, remove_russian_names, pass_args=True, pass_job_queue=True, pass_chat_data=True, database=db))

    # Start the bot
    logger.info("Starting bot...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
