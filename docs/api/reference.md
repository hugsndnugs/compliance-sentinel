# API Reference

Developer documentation for the Discord Legal Compliance Generator bot.

## Overview

The bot is built using:
- **discord.py** - Discord API wrapper
- **Python 3.10+** - Programming language

## Project Structure

```
discord-legal-compliance-generator/
├── bot/
│   ├── bot.py                 # Main bot instance
│   ├── commands/
│   │   ├── generate.py        # Generate command handlers
│   │   └── help.py            # Help command
│   ├── handlers/
│   │   ├── document_generator.py  # Template processing
│   │   └── form_handler.py        # Interactive forms
│   └── templates/             # Markdown templates
├── config/
│   └── config.py              # Configuration
└── main.py                    # Entry point
```

## Core Classes

### `LegalComplianceBot`

Main bot class extending `commands.Bot`.

**Location:** `bot/bot.py`

**Key Methods:**

- `setup_hook()` - Loads cogs and syncs slash commands
- `on_ready()` - Called when bot connects
- `on_command_error()` - Handles command errors

**Example:**

```python
from bot.bot import create_bot

bot = create_bot()
bot.run(DISCORD_BOT_TOKEN)
```

### `DocumentGenerator`

Handles template loading and document generation.

**Location:** `bot/handlers/document_generator.py`

**Methods:**

#### `load_template(document_type: str) -> str`

Loads a template file for the given document type.

**Parameters:**
- `document_type` (str): Type of document (e.g., "rules", "privacy_policy")

**Returns:**
- `str`: Template content as string

**Raises:**
- `FileNotFoundError`: If template file doesn't exist

**Example:**

```python
from bot.handlers.document_generator import DocumentGenerator

generator = DocumentGenerator()
template = generator.load_template("rules")
```

#### `generate_document(document_type: str, variables: Dict[str, Any]) -> str`

Generates a document by replacing template variables.

**Parameters:**
- `document_type` (str): Type of document to generate
- `variables` (Dict[str, Any]): Dictionary of variable names and values

**Returns:**
- `str`: Generated markdown document

**Example:**

```python
variables = {
    "server_name": "My Server",
    "contact_info": "admin@example.com",
    "rules": ["Rule 1", "Rule 2"]
}

document = generator.generate_document("rules", variables)
```

#### `get_available_document_types() -> list`

Returns list of available document types based on template files.

**Returns:**
- `list`: List of document type strings

### `FormHandler`

Manages interactive forms for document generation.

**Location:** `bot/handlers/form_handler.py`

**Attributes:**

- `document_generator` (DocumentGenerator): Document generator instance
- `active_forms` (Dict[int, Dict[str, Any]]): Active form data by user ID

**Methods:**

#### `get_document_type_embed() -> discord.Embed`

Creates an embed for document type selection.

**Returns:**
- `discord.Embed`: Embed with document type information

#### `get_document_type_view() -> discord.ui.View`

Creates a view with buttons for document type selection.

**Returns:**
- `discord.ui.View`: View with document type buttons

#### `_get_form_modal(document_type: str) -> discord.ui.Modal`

Gets the appropriate modal form for a document type.

**Parameters:**
- `document_type` (str): Type of document

**Returns:**
- `discord.ui.Modal`: Modal form for the document type

#### `_process_form(interaction, document_type, form_data)`

Processes submitted form and generates document.

**Parameters:**
- `interaction` (discord.Interaction): Discord interaction
- `document_type` (str): Type of document
- `form_data` (Dict[str, Any]): Form data dictionary

## Command Classes

### `GenerateCommands`

Command cog for generating documents.

**Location:** `bot/commands/generate.py`

**Commands:**

- `generate_slash()` - Slash command handler
- `generate_message()` - Message command handler

**Methods:**

#### `document_type_autocomplete(interaction, current) -> list[app_commands.Choice[str]]`

Autocomplete handler for document_type parameter.

**Parameters:**
- `interaction` (discord.Interaction): Discord interaction
- `current` (str): Current input text

**Returns:**
- `list[app_commands.Choice[str]]`: List of autocomplete choices

## Configuration

### `config.py`

Configuration constants and settings.

**Constants:**

- `DISCORD_BOT_TOKEN` (str): Bot token from environment
- `BOT_PREFIX` (str): Command prefix for message commands
- `DOCUMENT_TYPES` (Dict[str, str]): Mapping of document type keys to display names
- `TEMPLATES_DIR` (str): Path to templates directory

**Example:**

```python
from config.config import DOCUMENT_TYPES, TEMPLATES_DIR

# Access document types
for key, name in DOCUMENT_TYPES.items():
    print(f"{key}: {name}")

# Get templates directory
print(TEMPLATES_DIR)
```

## Template System

### Template Format

Templates use placeholder variables in format `{variable_name}`:

```markdown
# {server_name} - Server Rules

{contact_info}

## Rules
{formatted_rules}
```

### Variable Replacement

Variables are replaced using string substitution:

```python
template = "# {server_name} Rules"
document = template.replace("{server_name}", "My Server")
# Result: "# My Server Rules"
```

### List Formatting

Arrays are automatically formatted as markdown lists:

```python
rules = ["Rule 1", "Rule 2", "Rule 3"]
formatted = "\n".join(f"- {rule}" for rule in rules)
# Result: "- Rule 1\n- Rule 2\n- Rule 3"
```

## Extending the Bot

### Adding New Commands

Create a new command file in `bot/commands/`:

```python
from discord.ext import commands

class MyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="mycommand")
    async def my_command(self, ctx):
        await ctx.send("Hello!")
    
    @app_commands.command(name="mycommand")
    async def my_slash_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")

async def setup(bot):
    await bot.add_cog(MyCommands(bot))
```

Load in `bot/bot.py`:

```python
await self.load_extension("bot.commands.my_commands")
```

### Adding Event Handlers

Add to `LegalComplianceBot` class:

```python
async def on_member_join(self, member):
    """Called when a member joins a guild."""
    logger.info(f"{member} joined {member.guild}")
```

### Custom Error Handling

Extend `on_command_error`:

```python
async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    # Your custom error handling
    await super().on_command_error(ctx, error)
```

## Utilities

### Logging

The bot uses Python's `logging` module:

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Information message")
logger.error("Error message")
```

### Environment Variables

Load with `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
```

## Discord API Integration

### Intents

Required intents:

```python
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
```

### Slash Commands

Register and sync:

```python
@app_commands.command(name="command")
async def my_command(interaction: discord.Interaction):
    await interaction.response.send_message("Response")

# Sync on startup
synced = await bot.tree.sync()
```

### Modals

Create interactive forms:

```python
class MyModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="My Form")
        self.add_item(discord.ui.TextInput(label="Field"))
    
    async def on_submit(self, interaction):
        await interaction.response.send_message("Submitted")
```

## Best Practices

### 1. Error Handling

Always handle errors gracefully:

```python
try:
    document = generator.generate_document(type, data)
except FileNotFoundError:
    await interaction.response.send_message("Template not found")
except Exception as e:
    logger.error(f"Error: {e}")
    await interaction.response.send_message("An error occurred")
```

### 2. Type Hints

Use type hints for better code clarity:

```python
def generate_document(
    document_type: str,
    variables: Dict[str, Any]
) -> str:
    # Implementation
```

### 3. Documentation

Document your code:

```python
def my_function(param: str) -> str:
    """
    Brief description.
    
    Args:
        param: Parameter description
    
    Returns:
        Return value description
    """
    pass
```

### 4. Testing

Test your changes:

```python
# Test template loading
generator = DocumentGenerator()
template = generator.load_template("rules")
assert "{server_name}" in template

# Test document generation
variables = {"server_name": "Test Server"}
document = generator.generate_document("rules", variables)
assert "Test Server" in document
```

## Common Patterns

### Form Data Collection

```python
form_data = {
    "server_name": input_field.value,
    "optional_field": optional_field.value or "Default value",
    "list_field": [item.strip() for item in list_field.value.split("\n") if item.strip()]
}
```

### File Generation

```python
from io import BytesIO

document = generator.generate_document(type, data)
file = discord.File(
    fp=BytesIO(document.encode('utf-8')),
    filename=f"{document_type}.md"
)
await interaction.response.send_message(file=file)
```

### Ephemeral Responses

```python
await interaction.response.send_message(
    "Response",
    ephemeral=True  # Only visible to user
)
```

## Next Steps

- Review [Customization Guides](../customization/templates.md)
- Check [Troubleshooting](../troubleshooting.md) for common issues
- Explore the source code for more examples
