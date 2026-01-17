"""Main entry point for the Discord Legal Compliance Generator Bot."""

import asyncio
import logging
import sys
from bot.bot import create_bot
from config.config import DISCORD_BOT_TOKEN

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Main function to run the bot."""
    if not DISCORD_BOT_TOKEN:
        logger.error("DISCORD_BOT_TOKEN not found in environment variables!")
        logger.error("Please create a .env file with your bot token.")
        sys.exit(1)
    
    # Create and run the bot
    bot = create_bot()
    
    try:
        bot.run(DISCORD_BOT_TOKEN)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Error running bot: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
