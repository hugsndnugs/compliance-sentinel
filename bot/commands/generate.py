"""Generate command handlers for slash and message commands."""

import discord
from discord import app_commands
from discord.ext import commands
from bot.handlers.form_handler import FormHandler
from config.config import DOCUMENT_TYPES


class GenerateCommands(commands.Cog):
    """Commands for generating legal/compliance documents."""
    
    def __init__(self, bot):
        self.bot = bot
        self.form_handler = FormHandler()
    
    async def document_type_autocomplete(
        self,
        interaction: discord.Interaction,
        current: str
    ) -> list[app_commands.Choice[str]]:
        """Autocomplete handler for document_type parameter."""
        choices = []
        current_lower = current.lower()
        
        for key, display_name in DOCUMENT_TYPES.items():
            # Match against both key and display name
            if current_lower in key.lower() or current_lower in display_name.lower():
                choices.append(app_commands.Choice(name=display_name, value=key))
        
        # Return up to 25 choices (Discord's limit)
        return choices[:25]
    
    @app_commands.command(name="generate", description="Generate a legal/compliance document")
    @app_commands.describe(document_type="Type of document to generate (optional - use buttons if not specified)")
    @app_commands.autocomplete(document_type=document_type_autocomplete)
    async def generate_slash(
        self,
        interaction: discord.Interaction,
        document_type: str = None
    ):
        """Slash command to generate a document."""
        if document_type:
            # Direct document type specified
            if document_type not in DOCUMENT_TYPES:
                await interaction.response.send_message(
                    f"❌ Invalid document type. Available types: {', '.join(DOCUMENT_TYPES.keys())}",
                    ephemeral=True
                )
                return
            
            # Initialize form data and show modal
            self.form_handler.active_forms[interaction.user.id] = {
                "document_type": document_type,
                "data": {}
            }
            modal = self.form_handler._get_form_modal(document_type)
            await interaction.response.send_modal(modal)
        else:
            # Show document type selection
            embed = self.form_handler.get_document_type_embed()
            view = self.form_handler.get_document_type_view()
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    
    @commands.command(name="generate", aliases=["gen", "g"])
    async def generate_message(self, ctx: commands.Context, document_type: str = None):
        """Message command to generate a document."""
        if document_type:
            # Direct document type specified
            if document_type not in DOCUMENT_TYPES:
                available = ', '.join(DOCUMENT_TYPES.keys())
                await ctx.send(
                    f"❌ Invalid document type: `{document_type}`\n"
                    f"Available types: `{available}`"
                )
                return
            
            # For message commands, we need to use a button to trigger the modal
            # since modals can only be sent in response to interactions
            embed = discord.Embed(
                title=f"Generate {DOCUMENT_TYPES[document_type]}",
                description="Click the button below to start the form.",
                color=discord.Color.blue()
            )
            
            # Create a button that will trigger the modal
            class StartFormButton(discord.ui.Button):
                def __init__(self, form_handler, doc_type):
                    super().__init__(label="Start Form", style=discord.ButtonStyle.primary)
                    self.form_handler = form_handler
                    self.doc_type = doc_type
                
                async def callback(self, interaction: discord.Interaction):
                    # Initialize form data
                    self.form_handler.active_forms[interaction.user.id] = {
                        "document_type": self.doc_type,
                        "data": {}
                    }
                    modal = self.form_handler._get_form_modal(self.doc_type)
                    await interaction.response.send_modal(modal)
            
            view = discord.ui.View(timeout=300)
            view.add_item(StartFormButton(self.form_handler, document_type))
            await ctx.send(embed=embed, view=view)
        else:
            # Show document type selection
            embed = self.form_handler.get_document_type_embed()
            view = self.form_handler.get_document_type_view()
            await ctx.send(embed=embed, view=view)


async def setup(bot):
    """Setup function for the cog."""
    await bot.add_cog(GenerateCommands(bot))
