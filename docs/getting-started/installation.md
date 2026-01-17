# Installation

This guide will walk you through installing and setting up the Discord Legal Compliance Generator bot.

## Prerequisites

Before you begin, ensure you have:

- **Python 3.10 or higher** - Check your version with `python --version` or `python3 --version`
- **A Discord bot token** - Get one from the [Discord Developer Portal](https://discord.com/developers/applications)
- **Discord bot with appropriate permissions**:
  - Send Messages
  - Use Slash Commands
  - Embed Links
  - Attach Files

## Step 1: Clone or Download the Repository

Clone the repository using Git:

```bash
git clone https://github.com/YOUR_USERNAME/discord-legal-compliance-generator.git
cd discord-legal-compliance-generator
```

Or download and extract the ZIP file from GitHub.

## Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If you're using Python 3 specifically:

```bash
pip3 install -r requirements.txt
```

For a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Set Up Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your Discord bot token:
   ```env
   DISCORD_BOT_TOKEN=your_bot_token_here
   BOT_PREFIX=!
   ```

   Replace `your_bot_token_here` with your actual bot token from the Discord Developer Portal.

## Step 4: Get Your Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section in the left sidebar
4. Click "Add Bot" if you haven't already
5. Under "Token", click "Reset Token" or "Copy" to get your bot token
6. Paste this token into your `.env` file

!!! warning "Keep Your Token Secret"
    Never share your bot token publicly. If your token is exposed, reset it immediately in the Discord Developer Portal.

## Step 5: Invite Your Bot to Your Server

1. In the Discord Developer Portal, go to **OAuth2 > URL Generator**
2. Select the following scopes:
   - `bot`
   - `applications.commands`
3. Select the following bot permissions:
   - Send Messages
   - Use Slash Commands
   - Embed Links
   - Attach Files
4. Copy the generated URL and open it in your browser
5. Select your Discord server and authorize the bot

## Step 6: Run the Bot

Start the bot with:

```bash
python main.py
```

Or if using Python 3 specifically:

```bash
python3 main.py
```

You should see output indicating the bot has connected:

```
INFO - BotName#1234 has connected to Discord!
INFO - Bot is in X guild(s)
INFO - Synced X slash command(s)
```

## Verification

To verify the bot is working:

1. Go to your Discord server where the bot is present
2. Type `/generate` or `!generate`
3. You should see a menu with document type options

If the bot doesn't respond, check:

- The bot is online (green status indicator)
- The bot has proper permissions in the channel
- Your bot token is correct in the `.env` file
- The bot has the `applications.commands` scope

## Next Steps

- Configure additional settings in [Configuration](configuration.md)
- Learn how to use commands in [Usage Guide](../usage/commands.md)
- Customize templates in [Customization Guide](../customization/templates.md)

## Troubleshooting

If you encounter issues during installation, see the [Troubleshooting Guide](../troubleshooting.md) for common solutions.
