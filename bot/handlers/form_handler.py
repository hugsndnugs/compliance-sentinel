"""Handles interactive forms for collecting user input."""

import discord
from io import BytesIO
from typing import Dict, Any, Optional, Callable
from bot.handlers.document_generator import DocumentGenerator


class DocumentTypeButton(discord.ui.Button):
    """Button for selecting a document type."""
    
    def __init__(self, form_handler, doc_type: str, label: str):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.form_handler = form_handler
        self.doc_type = doc_type
    
    async def callback(self, interaction: discord.Interaction):
        """Handle button click."""
        await self.form_handler._handle_document_type_selection(interaction, self.doc_type)


class DocumentTypeView(discord.ui.View):
    """View containing document type selection buttons."""
    
    def __init__(self, form_handler):
        super().__init__(timeout=300)
        self.form_handler = form_handler
        
        document_types = [
            ("rules", "📋 Rules"),
            ("privacy_policy", "🔒 Privacy"),
            ("terms_of_service", "📜 ToS"),
            ("code_of_conduct", "✅ CoC"),
            ("staff_sops", "👥 SOPs"),
            ("moderation_guidelines", "⚖️ Moderation"),
            ("appeal_process", "📝 Appeal"),
        ]
        
        for doc_type, label in document_types:
            self.add_item(DocumentTypeButton(form_handler, doc_type, label))


class DynamicModal(discord.ui.Modal):
    """A modal that can have its on_submit callback set dynamically."""
    
    def __init__(self, title: str, callback_func):
        super().__init__(title=title)
        self._callback_func = callback_func
    
    async def on_submit(self, interaction: discord.Interaction):
        """Handle modal submission."""
        await self._callback_func(interaction)


class FormHandler:
    """Manages interactive forms for document generation."""
    
    def __init__(self):
        self.document_generator = DocumentGenerator()
        self.active_forms: Dict[int, Dict[str, Any]] = {}  # user_id -> form_data
    
    def get_document_type_embed(self) -> discord.Embed:
        """Create an embed for document type selection."""
        embed = discord.Embed(
            title="📄 Legal Compliance Document Generator",
            description="Select the type of document you want to generate:",
            color=discord.Color.blue()
        )
        
        document_types = {
            "rules": "📋 Server Rules",
            "privacy_policy": "🔒 Privacy Policy",
            "terms_of_service": "📜 Terms of Service",
            "code_of_conduct": "✅ Code of Conduct",
            "staff_sops": "👥 Staff SOPs",
            "moderation_guidelines": "⚖️ Moderation Guidelines",
            "appeal_process": "📝 Appeal Process",
        }
        
        for doc_type, display_name in document_types.items():
            embed.add_field(
                name=display_name,
                value=f"Type: `{doc_type}`",
                inline=False
            )
        
        embed.set_footer(text="Use the buttons below or type the document type name")
        return embed
    
    def get_document_type_view(self) -> discord.ui.View:
        """Create a view with buttons for document type selection."""
        view = DocumentTypeView(self)
        return view
    
    async def _handle_document_type_selection(self, interaction: discord.Interaction, document_type: str):
        """Handle document type button selection."""
        # Initialize form data for this user
        self.active_forms[interaction.user.id] = {
            "document_type": document_type,
            "data": {}
        }
        
        # Show the appropriate form modal
        modal = self._get_form_modal(document_type)
        await interaction.response.send_modal(modal)
    
    def _get_form_modal(self, document_type: str) -> discord.ui.Modal:
        """Get the appropriate modal form for a document type."""
        modals = {
            "rules": self._get_rules_modal,
            "privacy_policy": self._get_privacy_policy_modal,
            "terms_of_service": self._get_terms_modal,
            "code_of_conduct": self._get_code_of_conduct_modal,
            "staff_sops": self._get_staff_sops_modal,
            "moderation_guidelines": self._get_moderation_modal,
            "appeal_process": self._get_appeal_modal,
        }
        
        return modals.get(document_type, self._get_generic_modal)()
    
    def _get_rules_modal(self) -> discord.ui.Modal:
        """Modal for Server Rules."""
        server_name = discord.ui.TextInput(
            label="Server Name",
            placeholder="Enter your server name",
            required=True,
            max_length=100
        )
        
        contact_info = discord.ui.TextInput(
            label="Contact Information",
            placeholder="Email or Discord username for contact",
            required=False,
            max_length=200
        )
        
        rules = discord.ui.TextInput(
            label="Rules (one per line)",
            placeholder="Rule 1\nRule 2\nRule 3",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=2000
        )
        
        consequences = discord.ui.TextInput(
            label="Consequences for Violations",
            placeholder="e.g., Warning → Mute → Ban",
            style=discord.TextStyle.paragraph,
            required=False,
            max_length=500
        )
        
        async def callback(interaction: discord.Interaction):
            form_data = {
                "server_name": server_name.value,
                "contact_info": contact_info.value or "Contact server administrators",
                "rules": [r.strip() for r in rules.value.split("\n") if r.strip()],
                "consequences": consequences.value or "Violations may result in warnings, mutes, or bans at staff discretion."
            }
            await self._process_form(interaction, "rules", form_data)
        
        modal = DynamicModal(title="Generate Server Rules", callback_func=callback)
        modal.add_item(server_name)
        modal.add_item(contact_info)
        modal.add_item(rules)
        modal.add_item(consequences)
        return modal
    
    def _get_privacy_policy_modal(self) -> discord.ui.Modal:
        """Modal for Privacy Policy."""
        server_name = discord.ui.TextInput(
            label="Server Name",
            placeholder="Enter your server name",
            required=True,
            max_length=100
        )
        
        contact_email = discord.ui.TextInput(
            label="Contact Email",
            placeholder="privacy@example.com",
            required=False,
            max_length=200
        )
        
        data_collected = discord.ui.TextInput(
            label="Data Collected (one per line)",
            placeholder="Discord username\nMessages\nUser IDs",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        data_usage = discord.ui.TextInput(
            label="How Data is Used",
            placeholder="Describe how collected data is used",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        async def callback(interaction: discord.Interaction):
            form_data = {
                "server_name": server_name.value,
                "contact_email": contact_email.value or "Contact server administrators",
                "data_collected": [d.strip() for d in data_collected.value.split("\n") if d.strip()],
                "data_usage": data_usage.value
            }
            await self._process_form(interaction, "privacy_policy", form_data)
        
        modal = DynamicModal(title="Generate Privacy Policy", callback_func=callback)
        modal.add_item(server_name)
        modal.add_item(contact_email)
        modal.add_item(data_collected)
        modal.add_item(data_usage)
        return modal
    
    def _get_terms_modal(self) -> discord.ui.Modal:
        """Modal for Terms of Service."""
        server_name = discord.ui.TextInput(
            label="Server Name",
            placeholder="Enter your server name",
            required=True,
            max_length=100
        )
        
        contact_info = discord.ui.TextInput(
            label="Contact Information",
            placeholder="Email or Discord username",
            required=False,
            max_length=200
        )
        
        prohibited_activities = discord.ui.TextInput(
            label="Prohibited Activities (one per line)",
            placeholder="Harassment\nSpam\nNSFW content",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        user_obligations = discord.ui.TextInput(
            label="User Obligations",
            placeholder="Describe user responsibilities",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        async def callback(interaction: discord.Interaction):
            form_data = {
                "server_name": server_name.value,
                "contact_info": contact_info.value or "Contact server administrators",
                "prohibited_activities": [p.strip() for p in prohibited_activities.value.split("\n") if p.strip()],
                "user_obligations": user_obligations.value
            }
            await self._process_form(interaction, "terms_of_service", form_data)
        
        modal = DynamicModal(title="Generate Terms of Service", callback_func=callback)
        modal.add_item(server_name)
        modal.add_item(contact_info)
        modal.add_item(prohibited_activities)
        modal.add_item(user_obligations)
        return modal
    
    def _get_code_of_conduct_modal(self) -> discord.ui.Modal:
        """Modal for Code of Conduct."""
        server_name = discord.ui.TextInput(
            label="Server Name",
            placeholder="Enter your server name",
            required=True,
            max_length=100
        )
        
        expected_behavior = discord.ui.TextInput(
            label="Expected Behavior (one per line)",
            placeholder="Be respectful\nBe inclusive\nFollow Discord ToS",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        reporting_process = discord.ui.TextInput(
            label="Reporting Process",
            placeholder="How to report violations",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        contact_info = discord.ui.TextInput(
            label="Contact Information",
            placeholder="Email or Discord username",
            required=False,
            max_length=200
        )
        
        async def callback(interaction: discord.Interaction):
            form_data = {
                "server_name": server_name.value,
                "expected_behavior": [b.strip() for b in expected_behavior.value.split("\n") if b.strip()],
                "reporting_process": reporting_process.value,
                "contact_info": contact_info.value or "Contact server administrators"
            }
            await self._process_form(interaction, "code_of_conduct", form_data)
        
        modal = DynamicModal(title="Generate Code of Conduct", callback_func=callback)
        modal.add_item(server_name)
        modal.add_item(expected_behavior)
        modal.add_item(reporting_process)
        modal.add_item(contact_info)
        return modal
    
    def _get_staff_sops_modal(self) -> discord.ui.Modal:
        """Modal for Staff SOPs."""
        server_name = discord.ui.TextInput(
            label="Server Name",
            placeholder="Enter your server name",
            required=True,
            max_length=100
        )
        
        staff_roles = discord.ui.TextInput(
            label="Staff Roles (one per line)",
            placeholder="Administrator\nModerator\nSupport Staff",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        procedures = discord.ui.TextInput(
            label="Key Procedures (one per line)",
            placeholder="Handling reports\nEscalation process\nBan appeals",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        escalation_path = discord.ui.TextInput(
            label="Escalation Path",
            placeholder="Describe the escalation process",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        async def callback(interaction: discord.Interaction):
            form_data = {
                "server_name": server_name.value,
                "staff_roles": [r.strip() for r in staff_roles.value.split("\n") if r.strip()],
                "procedures": [p.strip() for p in procedures.value.split("\n") if p.strip()],
                "escalation_path": escalation_path.value
            }
            await self._process_form(interaction, "staff_sops", form_data)
        
        modal = DynamicModal(title="Generate Staff SOPs", callback_func=callback)
        modal.add_item(server_name)
        modal.add_item(staff_roles)
        modal.add_item(procedures)
        modal.add_item(escalation_path)
        return modal
    
    def _get_moderation_modal(self) -> discord.ui.Modal:
        """Modal for Moderation Guidelines."""
        server_name = discord.ui.TextInput(
            label="Server Name",
            placeholder="Enter your server name",
            required=True,
            max_length=100
        )
        
        moderation_actions = discord.ui.TextInput(
            label="Moderation Actions (one per line)",
            placeholder="Warning\nMute\nKick\nBan",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        warning_system = discord.ui.TextInput(
            label="Warning System",
            placeholder="Describe the warning system",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        ban_criteria = discord.ui.TextInput(
            label="Ban Criteria",
            placeholder="Describe when bans are issued",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        async def callback(interaction: discord.Interaction):
            form_data = {
                "server_name": server_name.value,
                "moderation_actions": [a.strip() for a in moderation_actions.value.split("\n") if a.strip()],
                "warning_system": warning_system.value,
                "ban_criteria": ban_criteria.value
            }
            await self._process_form(interaction, "moderation_guidelines", form_data)
        
        modal = DynamicModal(title="Generate Moderation Guidelines", callback_func=callback)
        modal.add_item(server_name)
        modal.add_item(moderation_actions)
        modal.add_item(warning_system)
        modal.add_item(ban_criteria)
        return modal
    
    def _get_appeal_modal(self) -> discord.ui.Modal:
        """Modal for Appeal Process."""
        server_name = discord.ui.TextInput(
            label="Server Name",
            placeholder="Enter your server name",
            required=True,
            max_length=100
        )
        
        appeal_requirements = discord.ui.TextInput(
            label="Appeal Requirements",
            placeholder="What information is needed for appeals",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        review_process = discord.ui.TextInput(
            label="Review Process",
            placeholder="How appeals are reviewed",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        timelines = discord.ui.TextInput(
            label="Timelines",
            placeholder="Response time, review duration, etc.",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        contact_info = discord.ui.TextInput(
            label="Contact Information",
            placeholder="How to submit appeals",
            required=False,
            max_length=200
        )
        
        async def callback(interaction: discord.Interaction):
            form_data = {
                "server_name": server_name.value,
                "appeal_requirements": appeal_requirements.value,
                "review_process": review_process.value,
                "timelines": timelines.value,
                "contact_info": contact_info.value or "Contact server administrators"
            }
            await self._process_form(interaction, "appeal_process", form_data)
        
        modal = DynamicModal(title="Generate Appeal Process", callback_func=callback)
        modal.add_item(server_name)
        modal.add_item(appeal_requirements)
        modal.add_item(review_process)
        modal.add_item(timelines)
        modal.add_item(contact_info)
        return modal
    
    def _get_generic_modal(self) -> discord.ui.Modal:
        """Generic modal for unknown document types."""
        server_name = discord.ui.TextInput(
            label="Server Name",
            placeholder="Enter your server name",
            required=True,
            max_length=100
        )
        
        content = discord.ui.TextInput(
            label="Content",
            placeholder="Enter document content",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=2000
        )
        
        async def callback(interaction: discord.Interaction):
            await interaction.response.send_message("Generic document generation not yet implemented.", ephemeral=True)
        
        modal = DynamicModal(title="Generate Document", callback_func=callback)
        modal.add_item(server_name)
        modal.add_item(content)
        return modal
    
    async def _process_form(self, interaction: discord.Interaction, document_type: str, form_data: Dict[str, Any]):
        """Process the submitted form and generate the document."""
        try:
            # Generate the document
            document = self.document_generator.generate_document(document_type, form_data)
            
            # Discord has a 2000 character limit for messages, so we'll send as a file if too long
            if len(document) > 1900:  # Leave some buffer
                # Send as a file
                file = discord.File(
                    fp=BytesIO(document.encode('utf-8')),
                    filename=f"{document_type}.md"
                )
                embed = discord.Embed(
                    title=f"✅ Generated {document_type.replace('_', ' ').title()}",
                    description=f"Your document has been generated! Here's the markdown file:",
                    color=discord.Color.green()
                )
                await interaction.response.send_message(embed=embed, file=file, ephemeral=True)
            else:
                # Send as a code block
                embed = discord.Embed(
                    title=f"✅ Generated {document_type.replace('_', ' ').title()}",
                    description="Your document has been generated:",
                    color=discord.Color.green()
                )
                await interaction.response.send_message(
                    embed=embed,
                    content=f"```markdown\n{document}\n```",
                    ephemeral=True
                )
            
            # Clean up form data
            if interaction.user.id in self.active_forms:
                del self.active_forms[interaction.user.id]
        
        except FileNotFoundError as e:
            await interaction.response.send_message(
                f"❌ Error: Template not found for {document_type}. Please contact the bot administrator.",
                ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Error generating document: {str(e)}",
                ephemeral=True
            )
