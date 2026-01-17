"""Main bot instance and setup."""

import discord
from discord.ext import commands
from config.config import DISCORD_BOT_TOKEN, BOT_PREFIX
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class LegalComplianceBot(commands.Bot):
    """Main bot class for the Legal Compliance Generator."""
    
    def __init__(self):
        # Set up intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        
        super().__init__(
            command_prefix=BOT_PREFIX,
            intents=intents,
            help_command=None  # We'll use our custom help command
        )
    
    async def setup_hook(self):
        """Called when the bot is starting up."""
        # Load cogs
        try:
            await self.load_extension("bot.commands.generate")
            await self.load_extension("bot.commands.help")
            logger.info("Successfully loaded all cogs")
        except Exception as e:
            logger.error(f"Error loading cogs: {e}")
        
        # Sync slash commands
        try:
            synced = await self.tree.sync()
            logger.info(f"Synced {len(synced)} slash command(s)")
        except Exception as e:
            logger.error(f"Error syncing commands: {e}")
    
    async def on_ready(self):
        """Called when the bot is ready."""
        logger.info(f"{self.user} has connected to Discord!")
        logger.info(f"Bot is in {len(self.guilds)} guild(s)")
        
        # Set bot status
        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="for /generate commands"
        )
        await self.change_presence(activity=activity)
    
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """Handle command errors."""
        if isinstance(error, commands.CommandNotFound):
            return  # Ignore command not found errors
        
        logger.error(f"Command error: {error}")
        
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"❌ Missing required argument: `{error.param.name}`")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"⏳ This command is on cooldown. Try again in {error.retry_after:.2f} seconds.")
        else:
            await ctx.send(f"❌ An error occurred: {str(error)}")
    
    async def on_error(self, event_method: str, *args, **kwargs):
        """Handle general errors."""
        logger.error(f"Error in {event_method}: {args}, {kwargs}")


def create_bot() -> LegalComplianceBot:
    """Create and return a bot instance."""
    return LegalComplianceBot()
