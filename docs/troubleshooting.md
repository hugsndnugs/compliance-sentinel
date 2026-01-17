# Troubleshooting

Common issues and solutions for the Discord Legal Compliance Generator bot.

## Bot Connection Issues

### Bot Doesn't Connect

**Symptoms:**
- Bot doesn't appear online in Discord
- No startup messages in console
- Connection errors in logs

**Solutions:**

1. **Check Bot Token:**
   ```bash
   # Verify .env file exists and has correct token
   cat .env
   ```
   Ensure `DISCORD_BOT_TOKEN` is set correctly.

2. **Verify Token Validity:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Check if token is still valid
   - Reset token if needed and update `.env`

3. **Check Internet Connection:**
   - Ensure your server has internet access
   - Check firewall settings
   - Verify Discord API is accessible

4. **Review Logs:**
   ```python
   # Check for specific error messages
   # Common errors:
   # - "401 Unauthorized" - Invalid token
   # - "403 Forbidden" - Missing permissions
   # - Connection timeout - Network issues
   ```

### Bot Connects But Immediately Disconnects

**Symptoms:**
- Bot appears online briefly then goes offline
- Repeated connection/disconnection cycles

**Solutions:**

1. **Check Bot Intents:**
   - Verify intents are enabled in Discord Developer Portal
   - Ensure `message_content` intent is enabled if using message commands

2. **Review Error Logs:**
   - Check for exception errors in console
   - Look for permission-related errors

3. **Verify Python Version:**
   ```bash
   python --version
   # Should be 3.10 or higher
   ```

## Command Issues

### Slash Commands Not Appearing

**Symptoms:**
- `/generate` command doesn't show in Discord
- Commands not in autocomplete

**Solutions:**

1. **Wait for Sync:**
   - Slash commands can take up to 1 hour to sync globally
   - Restart Discord client
   - Try in a server where bot was just added

2. **Check Bot Permissions:**
   - Verify bot has "Use Slash Commands" permission
   - Ensure bot has "applications.commands" scope

3. **Force Command Sync:**
   ```python
   # In bot.py, ensure setup_hook includes:
   synced = await self.tree.sync()
   logger.info(f"Synced {len(synced)} slash command(s)")
   ```

4. **Verify Command Registration:**
   - Check `bot/commands/generate.py` has `@app_commands.command` decorator
   - Ensure cog is loaded in `setup_hook()`

### Commands Not Responding

**Symptoms:**
- Bot doesn't respond to `/generate` or `!generate`
- No error messages

**Solutions:**

1. **Check Bot Status:**
   - Verify bot is online (green status)
   - Check bot is in the server/channel

2. **Verify Permissions:**
   - Bot needs "Send Messages" permission
   - Check channel permissions
   - Verify bot role has necessary permissions

3. **Check Command Prefix:**
   ```bash
   # Verify BOT_PREFIX in .env matches what you're using
   # Default is "!"
   ```

4. **Review Bot Logs:**
   - Check for error messages
   - Look for permission denied errors

### Form Modal Not Appearing

**Symptoms:**
- Clicking document type button doesn't show form
- Modal doesn't open

**Solutions:**

1. **Update Discord Client:**
   - Modals require recent Discord client version
   - Update Discord to latest version

2. **Check Interaction Response:**
   - Ensure modal is sent before timeout
   - Verify `interaction.response.send_modal()` is called

3. **Review Form Handler:**
   - Check `form_handler.py` for errors
   - Verify modal is properly constructed

## Document Generation Issues

### Template Not Found Error

**Symptoms:**
- Error: "Template not found for {document_type}"
- FileNotFoundError in logs

**Solutions:**

1. **Verify Template Exists:**
   ```bash
   ls bot/templates/
   # Should show all .md files
   ```

2. **Check Template Name:**
   - Template filename must match document type key
   - Example: `rules.md` for document type `"rules"`
   - Case-sensitive on some systems

3. **Verify Template Directory:**
   ```python
   # Check TEMPLATES_DIR in config/config.py
   # Should point to bot/templates/
   ```

### Variables Not Replacing

**Symptoms:**
- `{variable_name}` appears literally in generated document
- Placeholders not filled

**Solutions:**

1. **Check Variable Names:**
   - Variable names in template must match form data keys
   - Case-sensitive matching
   - Check for typos

2. **Verify Form Data:**
   ```python
   # In form_handler.py, ensure form_data dictionary
   # has keys matching template variables
   form_data = {
       "server_name": server_name.value,  # Matches {server_name}
       # ...
   }
   ```

3. **Check Template Encoding:**
   - Ensure template files are UTF-8 encoded
   - Check for hidden characters

### Document Too Long

**Symptoms:**
- Error about message length
- Document truncated

**Solutions:**

1. **Automatic File Handling:**
   - Bot automatically sends long documents as files
   - Check for `.md` file attachment

2. **Split Content:**
   - Break long documents into sections
   - Use multiple messages if needed

3. **Template Optimization:**
   - Remove unnecessary content
   - Use concise formatting

## Configuration Issues

### Environment Variables Not Loading

**Symptoms:**
- Bot token not found
- Configuration errors

**Solutions:**

1. **Verify .env File:**
   ```bash
   # Check file exists
   ls -la .env
   
   # Verify format (no spaces around =)
   DISCORD_BOT_TOKEN=your_token_here
   BOT_PREFIX=!
   ```

2. **Check python-dotenv:**
   ```bash
   pip install python-dotenv
   ```

3. **Verify Loading:**
   ```python
   # In config.py, ensure:
   from dotenv import load_dotenv
   load_dotenv()
   ```

### Bot Prefix Not Working

**Symptoms:**
- `!generate` doesn't work
- Wrong prefix expected

**Solutions:**

1. **Check .env File:**
   ```env
   BOT_PREFIX=!
   # Or your preferred prefix
   ```

2. **Restart Bot:**
   - Configuration loads on startup
   - Restart after changing prefix

3. **Verify Message Content Intent:**
   - Required for message commands
   - Enable in Discord Developer Portal

## Permission Issues

### Missing Permissions Error

**Symptoms:**
- "Missing Permissions" error
- Bot can't send messages

**Solutions:**

1. **Check Bot Permissions:**
   - Server Settings → Roles → Bot Role
   - Enable: Send Messages, Embed Links, Attach Files

2. **Channel Permissions:**
   - Right-click channel → Edit Channel → Permissions
   - Ensure bot role has necessary permissions

3. **Verify Invite URL:**
   - Re-invite bot with correct permissions
   - Use OAuth2 URL Generator in Developer Portal

## Performance Issues

### Bot Slow to Respond

**Symptoms:**
- Commands take long to process
- Delayed responses

**Solutions:**

1. **Check System Resources:**
   - Monitor CPU and memory usage
   - Check for resource constraints

2. **Review Logging:**
   - Excessive logging can slow bot
   - Adjust log level if needed

3. **Template Size:**
   - Large templates may slow generation
   - Optimize template content

### High Memory Usage

**Symptoms:**
- Bot uses excessive memory
- System slowdown

**Solutions:**

1. **Check Active Forms:**
   - `active_forms` dictionary stores form data
   - Forms timeout after 5 minutes
   - Consider reducing timeout if needed

2. **Template Caching:**
   - Templates are loaded on-demand
   - Consider caching for frequently used templates

## Development Issues

### Import Errors

**Symptoms:**
- `ModuleNotFoundError`
- Import failures

**Solutions:**

1. **Verify Installation:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Check Python Path:**
   ```bash
   # Run from project root
   python main.py
   ```

3. **Virtual Environment:**
   ```bash
   # Ensure virtual environment is activated
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

### Syntax Errors

**Symptoms:**
- Python syntax errors
- Indentation errors

**Solutions:**

1. **Check Python Version:**
   ```bash
   python --version
   # Should be 3.10+
   ```

2. **Use Linter:**
   ```bash
   pip install flake8
   flake8 bot/
   ```

3. **Verify Indentation:**
   - Use consistent indentation (4 spaces recommended)
   - Check for mixed tabs/spaces

## Getting Help

### Before Asking for Help

1. **Check Logs:**
   - Review console output
   - Look for error messages

2. **Verify Setup:**
   - Follow installation guide
   - Check all prerequisites

3. **Search Issues:**
   - Check GitHub issues
   - Search error messages

### Providing Information

When reporting issues, include:

- **Error Messages:** Full error text
- **Logs:** Relevant log output
- **Steps to Reproduce:** What you did
- **Expected Behavior:** What should happen
- **Actual Behavior:** What actually happened
- **Environment:** Python version, OS, discord.py version

### Useful Commands

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Verify bot token format
echo $DISCORD_BOT_TOKEN  # Should not be empty

# Test template loading
python -c "from bot.handlers.document_generator import DocumentGenerator; d = DocumentGenerator(); print(d.load_template('rules'))"
```

## Common Error Messages

### "401 Unauthorized"
- Invalid or expired bot token
- Solution: Reset token in Developer Portal

### "403 Forbidden"
- Missing bot permissions
- Solution: Re-invite bot with correct permissions

### "Command not found"
- Slash commands not synced
- Solution: Wait for sync or restart bot

### "Template not found"
- Missing template file
- Solution: Verify template exists in `bot/templates/`

### "Missing required argument"
- Incomplete command usage
- Solution: Check command syntax in documentation

## Next Steps

- Review [Installation Guide](getting-started/installation.md)
- Check [Configuration](getting-started/configuration.md)
- See [Usage Examples](usage/examples.md)
