# Configuration

This guide covers all configuration options for the Discord Legal Compliance Generator bot.

## Environment Variables

The bot uses environment variables for configuration. These are stored in a `.env` file in the root directory.

### Required Configuration

#### `DISCORD_BOT_TOKEN`

Your Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

```env
DISCORD_BOT_TOKEN=your_bot_token_here
```

!!! danger "Security Warning"
    Never commit your `.env` file to version control. It's already included in `.gitignore` for your protection.

### Optional Configuration

#### `BOT_PREFIX`

The prefix for message commands (default: `!`).

```env
BOT_PREFIX=!
```

Examples:
- `BOT_PREFIX=!` - Use `!generate` for commands
- `BOT_PREFIX=.` - Use `.generate` for commands
- `BOT_PREFIX=bot!` - Use `bot!generate` for commands

## Configuration File

The main configuration is managed in `config/config.py`. This file contains:

### Document Types

The available document types are defined in `DOCUMENT_TYPES`:

```python
DOCUMENT_TYPES = {
    "rules": "Server Rules",
    "privacy_policy": "Privacy Policy",
    "terms_of_service": "Terms of Service",
    "code_of_conduct": "Code of Conduct",
    "staff_sops": "Staff SOPs",
    "moderation_guidelines": "Moderation Guidelines",
    "appeal_process": "Appeal Process",
}
```

To add or modify document types, edit this dictionary. See [Adding New Document Types](../customization/adding-documents.md) for detailed instructions.

### Template Directory

The template directory path is automatically configured:

```python
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bot", "templates")
```

Templates are stored in `bot/templates/` as markdown files. See [Template Customization](../customization/templates.md) for more information.

## Bot Permissions

Ensure your bot has the following permissions in your Discord server:

### Required Permissions

- **Send Messages** - To send command responses and generated documents
- **Use Slash Commands** - To register and respond to slash commands
- **Embed Links** - To send rich embeds with document type selection
- **Attach Files** - To send generated documents as markdown files

### Recommended Permissions

- **Read Message History** - To see previous messages in channels
- **Add Reactions** - For better user experience (if you add reaction-based features)

## Bot Intents

The bot uses the following Discord intents (configured in `bot/bot.py`):

- **Default Intents** - Standard bot functionality
- **Message Content Intent** - Required to read message commands
- **Guilds Intent** - To access server information

!!! note "Intent Requirements"
    If you're using Discord.py 2.0+, message content intent must be enabled in the Discord Developer Portal under your bot's settings.

## Changing the Bot Prefix

To change the command prefix:

1. Edit your `.env` file:
   ```env
   BOT_PREFIX=your_preferred_prefix
   ```

2. Restart the bot

The new prefix will be active immediately after restart.

## Customizing Document Types

To add, remove, or modify document types:

1. Edit `config/config.py` and update the `DOCUMENT_TYPES` dictionary
2. Create or modify template files in `bot/templates/`
3. Add form handlers in `bot/handlers/form_handler.py` (if adding new types)
4. Restart the bot

See [Adding New Document Types](../customization/adding-documents.md) for a complete guide.

## Logging Configuration

Logging is configured in `bot/bot.py`. The default configuration:

- **Level**: INFO
- **Format**: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`

To change logging level, edit `bot/bot.py`:

```python
logging.basicConfig(
    level=logging.DEBUG,  # Change to DEBUG, WARNING, or ERROR
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## Production Considerations

For production deployments:

1. **Use Environment Variables** - Never hardcode tokens or secrets
2. **Enable Logging** - Set up proper log rotation and monitoring
3. **Use Process Managers** - Consider using `systemd`, `pm2`, or `supervisord`
4. **Monitor Resources** - Set up alerts for bot downtime
5. **Backup Templates** - Keep backups of your custom templates

## Next Steps

- Learn about [Command Usage](../usage/commands.md)
- Explore [Template Customization](../customization/templates.md)
- Check out [Troubleshooting](../troubleshooting.md) for common issues
