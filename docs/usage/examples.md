# Usage Examples

Step-by-step examples for using the Discord Legal Compliance Generator bot.

## Example 1: Generating Server Rules

### Using Slash Commands

1. Type `/generate rules` in your Discord channel
2. A modal form will appear with the following fields:
   - **Server Name**: "My Awesome Community"
   - **Contact Information**: "admin@example.com"
   - **Rules**: 
     ```
     Be respectful to all members
     No spam or self-promotion
     Keep discussions on-topic
     No NSFW content
     Follow Discord Terms of Service
     ```
   - **Consequences**: "First offense: Warning. Second offense: Mute. Third offense: Ban."
3. Click "Submit"
4. Receive your generated Server Rules document

### Using Message Commands

1. Type `!generate rules` in your Discord channel
2. Click the "Start Form" button that appears
3. Fill out the same form as above
4. Submit and receive your document

## Example 2: Creating a Privacy Policy

### Step-by-Step

1. **Initiate the command:**
   ```
   /generate privacy_policy
   ```

2. **Fill out the form:**
   - **Server Name**: "Tech Community Server"
   - **Contact Email**: "privacy@techcommunity.com"
   - **Data Collected**:
     ```
     Discord username and user ID
     Messages sent in public channels
     Profile information (avatar, status)
     Server join/leave timestamps
     ```
   - **How Data is Used**: "We collect this data to moderate the server, enforce rules, and improve user experience. Data is stored securely and not shared with third parties."

3. **Submit and review** the generated Privacy Policy

## Example 3: Setting Up Terms of Service

### Complete Workflow

```bash
# 1. Run the command
/generate terms_of_service

# 2. Form fields to fill:
```

**Form Input:**
- Server Name: "Gaming Community"
- Contact Information: "support@gamingcommunity.com"
- Prohibited Activities:
  ```
  Harassment or bullying
  Spam or advertising
  Sharing illegal content
  Impersonation
  Cheating or exploiting
  ```
- User Obligations: "Users must follow all server rules, respect other members, and comply with Discord's Terms of Service. Violations may result in warnings, mutes, or bans."

**Result:** A complete Terms of Service document ready for review.

## Example 4: Code of Conduct Generation

### Quick Example

```
/generate code_of_conduct
```

**Form Data:**
- Server Name: "Open Source Community"
- Expected Behavior:
  ```
  Be respectful and inclusive
  Welcome newcomers
  Provide constructive feedback
  Follow the project's contribution guidelines
  ```
- Reporting Process: "Report violations to moderators via DM or use the #report channel. All reports are confidential and reviewed within 24 hours."
- Contact Information: "mods@opensource.com"

## Example 5: Staff SOPs Document

### For Server Administrators

1. **Command:**
   ```
   !generate staff_sops
   ```

2. **Complete the form:**
   - Server Name: "Community Server"
   - Staff Roles:
     ```
     Administrator
     Moderator
     Support Staff
     Event Coordinator
     ```
   - Key Procedures:
     ```
     Handle reports within 24 hours
     Document all moderation actions
     Escalate serious issues to administrators
     Review ban appeals weekly
     ```
   - Escalation Path: "Support Staff → Moderator → Administrator → Server Owner"

## Example 6: Moderation Guidelines

### Creating Clear Guidelines

```
/generate moderation_guidelines
```

**Input:**
- Server Name: "Art Community"
- Moderation Actions:
  ```
  Verbal Warning
  Written Warning
  Temporary Mute (1-24 hours)
  Temporary Ban (1-7 days)
  Permanent Ban
  ```
- Warning System: "Users receive 3 warnings before a temporary ban. Warnings expire after 30 days of good behavior."
- Ban Criteria: "Permanent bans are issued for severe violations including harassment, illegal content, or repeated rule violations after multiple warnings."

## Example 7: Appeal Process

### Setting Up Appeals

```
/generate appeal_process
```

**Form Fields:**
- Server Name: "Community Server"
- Appeal Requirements: "Include your Discord username, reason for ban, and explanation of why you should be unbanned."
- Review Process: "Appeals are reviewed by a panel of 3 moderators. Majority vote determines the outcome."
- Timelines: "Appeals are reviewed within 7 business days. You will receive a response via DM."
- Contact Information: "Submit appeals to appeals@community.com or use the appeal form on our website."

## Interactive Selection Menu

### Using the Button Menu

1. Type `/generate` without specifying a document type
2. A menu with buttons appears:
   - 📋 Rules
   - 🔒 Privacy
   - 📜 ToS
   - ✅ CoC
   - 👥 SOPs
   - ⚖️ Moderation
   - 📝 Appeal
3. Click the button for your desired document type
4. Complete the form that appears

## Best Practices

### 1. Prepare Your Information

Before running the command, gather:
- Your server name
- Contact information
- Specific rules, policies, or procedures
- Any custom requirements

### 2. Review Generated Documents

Always review and customize generated documents:
- Check for accuracy
- Add server-specific details
- Ensure legal compliance (consult a lawyer for legal documents)
- Format for your server's needs

### 3. Save Your Documents

- Download generated `.md` files
- Store them in a secure location
- Keep backups
- Update them as your server evolves

### 4. Customize Templates

For frequently used documents, consider customizing templates:
- Edit files in `bot/templates/`
- Add your server's branding
- Include standard clauses
- See [Template Customization](../customization/templates.md)

## Common Workflows

### Setting Up a New Server

1. Generate Server Rules
2. Create Terms of Service
3. Set up Privacy Policy
4. Write Code of Conduct
5. Create Moderation Guidelines
6. Set up Appeal Process
7. Generate Staff SOPs

### Updating Existing Documents

1. Generate a new version of the document
2. Compare with your current document
3. Merge changes as needed
4. Update your server's documentation

### Bulk Generation

Generate all documents in sequence:
```
/generate rules
/generate privacy_policy
/generate terms_of_service
/generate code_of_conduct
/generate moderation_guidelines
/generate appeal_process
/generate staff_sops
```

## Troubleshooting Examples

### Command Not Working

**Problem:** Bot doesn't respond to `/generate`

**Solution:**
- Check bot is online
- Verify bot has "Use Slash Commands" permission
- Wait a few minutes for slash commands to sync
- Try `!generate` as an alternative

### Form Not Appearing

**Problem:** Modal form doesn't show up

**Solution:**
- Ensure you're using the latest Discord client
- Check bot has proper permissions
- Try using slash commands instead of message commands

### Document Too Long

**Problem:** Generated document exceeds Discord's message limit

**Solution:**
- The bot automatically sends long documents as files
- Download the `.md` file attachment
- Open in a markdown editor for viewing

## Next Steps

- Learn about [Command Reference](commands.md) for all available options
- Explore [Customization](../customization/templates.md) to tailor documents
- Check [API Reference](../api/reference.md) for developers
