import logging
import telegram
from telegram.ext import Updater, MessageHandler, Filters

from config import Config

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def remove_russian_names(update, context):
    """Remove users with Russian alphabet in their names from the Telegram channel."""
    user_name = update.message.from_user.first_name
    if any(c.isalpha() and ord(c) >= 1040 for c in user_name):
        context.bot.kick_chat_member(update.message.chat_id, update.message.from_user.id)

def main():
    """Start the Telegram bot."""
    # Create the Telegram bot
    updater = Updater(Config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add message handler to remove users with Russian alphabet in their names
    dp.add_handler(MessageHandler(Filters.text, remove_russian_names))

    # Start the bot
    logger.info("Starting bot...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
