# Discord Legal Compliance Generator Bot

A Discord bot that automatically generates legal and compliance documents for Discord servers, including rules, privacy policies, terms of service, codes of conduct, staff SOPs, moderation guidelines, and appeal processes.

## Features

- **Multiple Document Types**: Generate 7 different types of legal/compliance documents
- **Interactive Forms**: User-friendly Discord modals for collecting information
- **Template-Based**: Uses customizable markdown templates
- **Dual Command Support**: Both slash commands (`/generate`) and message commands (`!generate`)
- **Markdown Output**: Generates properly formatted markdown documents

## Supported Document Types

1. **Server Rules** - Community rules and guidelines
2. **Privacy Policy** - Data collection and usage policies
3. **Terms of Service** - User agreements and terms
4. **Code of Conduct** - Expected behavior and community standards
5. **Staff SOPs** - Standard Operating Procedures for staff members
6. **Moderation Guidelines** - Moderation policies and procedures
7. **Appeal Process** - Process for appealing moderation actions

## Prerequisites

- Python 3.10 or higher
- A Discord bot token (get one from [Discord Developer Portal](https://discord.com/developers/applications))
- Discord bot with appropriate permissions:
  - Send Messages
  - Use Slash Commands
  - Embed Links
  - Attach Files

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy `.env.example` to `.env`
   - Edit `.env` and add your Discord bot token:
     ```
     DISCORD_BOT_TOKEN=your_bot_token_here
     BOT_PREFIX=!
     ```

4. **Invite your bot to your Discord server**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Select your application
   - Go to OAuth2 > URL Generator
   - Select scopes: `bot` and `applications.commands`
   - Select bot permissions: `Send Messages`, `Use Slash Commands`, `Embed Links`, `Attach Files`
   - Copy the generated URL and open it in your browser to invite the bot

## Usage

### Running the Bot

```bash
python main.py
```

### Commands

#### Slash Commands

- `/generate` - Show document type selection menu
- `/generate <document_type>` - Directly start generating a specific document type
- `/help` - Show help information

#### Message Commands

- `!generate` - Show document type selection menu
- `!generate <document_type>` - Directly start generating a specific document type
- `!help` - Show help information

### Example Usage

1. Type `/generate` or `!generate` in your Discord server
2. Select a document type from the buttons or specify it directly
3. Fill out the interactive form with your server's information
4. Receive your generated markdown document

### Document Type Examples

- `/generate rules` - Generate server rules
- `/generate privacy_policy` - Generate privacy policy
- `!generate code_of_conduct` - Generate code of conduct
- `!generate staff_sops` - Generate staff SOPs

## Project Structure

```
discord-legal-compliance-generator/
├── bot/
│   ├── __init__.py
│   ├── bot.py                 # Main bot instance
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── generate.py        # Generate command handlers
│   │   └── help.py            # Help command
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── document_generator.py  # Template processing
│   │   └── form_handler.py        # Interactive forms
│   └── templates/
│       ├── rules.md
│       ├── privacy_policy.md
│       ├── terms_of_service.md
│       ├── code_of_conduct.md
│       ├── staff_sops.md
│       ├── moderation_guidelines.md
│       └── appeal_process.md
├── config/
│   └── config.py              # Configuration
├── requirements.txt
├── .env.example
├── README.md
└── main.py                    # Entry point
```

## Customization

### Modifying Templates

You can customize the document templates by editing the markdown files in `bot/templates/`. Templates use placeholder variables in the format `{variable_name}` that are replaced with user-provided data.

### Changing Bot Prefix

Edit the `BOT_PREFIX` in your `.env` file or `config/config.py`.

### Adding New Document Types

1. Create a new template file in `bot/templates/`
2. Add the document type to `DOCUMENT_TYPES` in `config/config.py`
3. Add a modal handler in `bot/handlers/form_handler.py`
4. Update the form handler to include the new document type

## Troubleshooting

### Bot doesn't respond to commands

- Ensure the bot is online and has proper permissions
- Check that slash commands are synced (they sync automatically on startup)
- Verify your bot token is correct in the `.env` file

### Commands not showing up

- Slash commands may take a few minutes to appear globally
- Try restarting Discord or using the bot in a server where it's already present
- Ensure the bot has the `applications.commands` scope

### Template errors

- Verify all template files exist in `bot/templates/`
- Check that template variables match the form data keys
- Review the logs for specific error messages

## License

This project is provided as-is for educational and practical use.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Support

For issues or questions, please open an issue on the repository or contact the bot administrator.

---

**Note**: This bot generates template-based documents. For legal matters, it's recommended to have documents reviewed by a legal professional.
