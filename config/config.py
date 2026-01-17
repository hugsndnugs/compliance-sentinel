"""Configuration constants for the bot."""

import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")

# Bot Prefix for message commands
BOT_PREFIX = os.getenv("BOT_PREFIX", "!")

# Document Types
DOCUMENT_TYPES = {
    "rules": "Server Rules",
    "privacy_policy": "Privacy Policy",
    "terms_of_service": "Terms of Service",
    "code_of_conduct": "Code of Conduct",
    "staff_sops": "Staff SOPs",
    "moderation_guidelines": "Moderation Guidelines",
    "appeal_process": "Appeal Process",
}

# Template Directory
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bot", "templates")
