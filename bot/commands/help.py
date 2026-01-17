"""Help command for the bot."""

import discord
from discord import app_commands
from discord.ext import commands
from config.config import DOCUMENT_TYPES, BOT_PREFIX


class HelpCommands(commands.Cog):
    """Help command for the bot."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="help", description="Show help information about the bot")
    async def help_slash(self, interaction: discord.Interaction):
        """Slash command to show help."""
        embed = self._create_help_embed()
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @commands.command(name="help", aliases=["h", "commands"])
    async def help_message(self, ctx: commands.Context):
        """Message command to show help."""
        embed = self._create_help_embed()
        await ctx.send(embed=embed)
    
    def _create_help_embed(self) -> discord.Embed:
        """Create the help embed."""
        embed = discord.Embed(
            title="📚 Legal Compliance Generator - Help",
            description="Generate legal and compliance documents for your Discord server.",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="📋 Available Commands",
            value=(
                f"`/generate` or `{BOT_PREFIX}generate` - Generate a document\n"
                f"`/help` or `{BOT_PREFIX}help` - Show this help message"
            ),
            inline=False
        )
        
        embed.add_field(
            name="📄 Available Document Types",
            value="\n".join([
                f"• **{display_name}** (`{doc_type}`)"
                for doc_type, display_name in DOCUMENT_TYPES.items()
            ]),
            inline=False
        )
        
        embed.add_field(
            name="🚀 Usage Examples",
            value=(
                f"`/generate rules` - Generate server rules\n"
                f"`/generate` - Show document type selection\n"
                f"`{BOT_PREFIX}generate privacy_policy` - Generate privacy policy\n"
                f"`{BOT_PREFIX}generate code_of_conduct` - Generate code of conduct"
            ),
            inline=False
        )
        
        embed.add_field(
            name="💡 How It Works",
            value=(
                "1. Use `/generate` or `!generate` to start\n"
                "2. Select a document type\n"
                "3. Fill out the interactive form\n"
                "4. Receive your generated markdown document"
            ),
            inline=False
        )
        
        embed.set_footer(text="Need more help? Contact the server administrators")
        
        return embed


async def setup(bot):
    """Setup function for the cog."""
    await bot.add_cog(HelpCommands(bot))
