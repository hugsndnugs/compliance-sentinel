# Commands Reference

Complete reference for all bot commands, including slash commands and message commands.

## Command Overview

The bot supports two types of commands:

- **Slash Commands** - Modern Discord slash commands (e.g., `/generate`)
- **Message Commands** - Traditional prefix-based commands (e.g., `!generate`)

Both command types provide the same functionality.

## Generate Command

The main command for generating legal/compliance documents.

### Slash Command

```
/generate [document_type]
```

### Message Command

```
!generate [document_type]
```

Or using your configured prefix:

```
<prefix>generate [document_type]
```

### Parameters

#### `document_type` (optional)

The type of document to generate. If omitted, a selection menu will be displayed.

**Available document types:**

| Type | Display Name | Description |
|------|-------------|-------------|
| `rules` | Server Rules | Community rules and guidelines |
| `privacy_policy` | Privacy Policy | Data collection and usage policies |
| `terms_of_service` | Terms of Service | User agreements and terms |
| `code_of_conduct` | Code of Conduct | Expected behavior and community standards |
| `staff_sops` | Staff SOPs | Standard Operating Procedures for staff |
| `moderation_guidelines` | Moderation Guidelines | Moderation policies and procedures |
| `appeal_process` | Appeal Process | Process for appealing moderation actions |

### Usage Examples

#### Without Document Type

Shows a selection menu with all available document types:

```
/generate
```

or

```
!generate
```

#### With Document Type

Directly starts the form for a specific document type:

```
/generate rules
```

```
/generate privacy_policy
```

```
!generate code_of_conduct
```

```
!generate staff_sops
```

### Autocomplete

When using slash commands, the `document_type` parameter supports autocomplete. Start typing and Discord will suggest matching document types.

## Help Command

Get help information about the bot.

### Slash Command

```
/help
```

### Message Command

```
!help
```

Displays information about:
- Available commands
- How to use the bot
- Supported document types
- Quick examples

## Command Workflow

### Step 1: Initiate Command

Type `/generate` or `!generate` in a channel where the bot has permissions.

### Step 2: Select Document Type

If you didn't specify a document type:

1. A menu with buttons will appear
2. Click a button to select a document type
3. Or type the document type name directly in the command

### Step 3: Fill Out Form

An interactive modal form will appear with fields specific to the document type:

- **Server Name** - Required for all document types
- **Document-Specific Fields** - Varies by document type

### Step 4: Receive Document

After submitting the form:

- Short documents (< 1900 characters) are sent as formatted markdown code blocks
- Longer documents are sent as `.md` file attachments

## Document Type Forms

Each document type has a customized form. Here's what each form collects:

### Server Rules

- Server Name (required)
- Contact Information (optional)
- Rules (required, one per line)
- Consequences for Violations (optional)

### Privacy Policy

- Server Name (required)
- Contact Email (optional)
- Data Collected (required, one per line)
- How Data is Used (required)

### Terms of Service

- Server Name (required)
- Contact Information (optional)
- Prohibited Activities (required, one per line)
- User Obligations (required)

### Code of Conduct

- Server Name (required)
- Expected Behavior (required, one per line)
- Reporting Process (required)
- Contact Information (optional)

### Staff SOPs

- Server Name (required)
- Staff Roles (required, one per line)
- Key Procedures (required, one per line)
- Escalation Path (required)

### Moderation Guidelines

- Server Name (required)
- Moderation Actions (required, one per line)
- Warning System (required)
- Ban Criteria (required)

### Appeal Process

- Server Name (required)
- Appeal Requirements (required)
- Review Process (required)
- Timelines (required)
- Contact Information (optional)

## Command Permissions

The bot requires the following permissions to function:

- **Send Messages** - To respond to commands
- **Use Slash Commands** - To register slash commands
- **Embed Links** - To display selection menus
- **Attach Files** - To send generated documents

## Command Behavior

### Ephemeral Responses

Slash command responses are sent as ephemeral messages by default, meaning only you can see them. This keeps the channel clean.

### Message Commands

Message command responses are visible to everyone in the channel.

### Timeouts

- Button views timeout after 5 minutes (300 seconds)
- If a view times out, you'll need to run the command again

### Error Handling

If an error occurs:

- The bot will send an error message explaining what went wrong
- Check the bot's console logs for detailed error information
- See [Troubleshooting](../troubleshooting.md) for common issues

## Tips and Best Practices

1. **Use Slash Commands** - They provide autocomplete and better user experience
2. **Be Specific** - Include the document type in your command to skip the selection menu
3. **Fill Forms Completely** - Required fields are marked, but optional fields improve document quality
4. **Review Generated Documents** - Always review and customize generated documents before using them
5. **Save Documents** - Download or copy generated documents for your records

## Next Steps

- See [Usage Examples](examples.md) for detailed walkthroughs
- Learn about [Customization](../customization/templates.md)
- Check [Troubleshooting](../troubleshooting.md) if you encounter issues
