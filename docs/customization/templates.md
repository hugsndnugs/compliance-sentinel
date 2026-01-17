# Template Customization

Learn how to customize the document templates to match your server's needs and branding.

## Template Location

All templates are stored in the `bot/templates/` directory as Markdown files:

```
bot/templates/
├── rules.md
├── privacy_policy.md
├── terms_of_service.md
├── code_of_conduct.md
├── staff_sops.md
├── moderation_guidelines.md
└── appeal_process.md
```

## Template Structure

Templates use placeholder variables in the format `{variable_name}` that are replaced with user-provided data during document generation.

### Example Template

```markdown
# {server_name} - Server Rules

## Contact Information

{contact_info}

## Rules

{formatted_rules}

## Consequences

{consequences}
```

### Variable Replacement

When a user fills out a form:
- `{server_name}` → "My Awesome Server"
- `{contact_info}` → "admin@example.com"
- `{formatted_rules}` → Formatted list of rules
- `{consequences}` → "Warning → Mute → Ban"

## Customizing Templates

### Step 1: Locate the Template

Find the template file you want to customize in `bot/templates/`.

### Step 2: Edit the Template

Open the template file in a text editor and modify as needed.

### Example: Customizing Server Rules

**Original template:**
```markdown
# {server_name} - Server Rules

{contact_info}

## Rules
{formatted_rules}

## Consequences
{consequences}
```

**Customized template:**
```markdown
# Welcome to {server_name}!

## 📋 Server Rules

Please read and follow these rules to ensure a positive experience for everyone.

### Contact Us
{contact_info}

### Our Rules
{formatted_rules}

### Enforcement
{consequences}

---
*Last updated: [Add date]*
*Questions? Contact the moderation team.*
```

### Step 3: Save and Restart

1. Save your changes
2. Restart the bot
3. Test by generating a document

## Available Variables

Each document type has specific variables. Here's a reference:

### Server Rules (`rules.md`)

- `{server_name}` - Server name
- `{contact_info}` - Contact information
- `{rules}` - List of rules (array)
- `{formatted_rules}` - Formatted rules list
- `{consequences}` - Consequences for violations

### Privacy Policy (`privacy_policy.md`)

- `{server_name}` - Server name
- `{contact_email}` - Contact email
- `{data_collected}` - List of collected data (array)
- `{formatted_data_collected}` - Formatted data list
- `{data_usage}` - How data is used

### Terms of Service (`terms_of_service.md`)

- `{server_name}` - Server name
- `{contact_info}` - Contact information
- `{prohibited_activities}` - List of prohibited activities (array)
- `{formatted_prohibited_activities}` - Formatted prohibited activities
- `{user_obligations}` - User obligations

### Code of Conduct (`code_of_conduct.md`)

- `{server_name}` - Server name
- `{expected_behavior}` - List of expected behaviors (array)
- `{formatted_expected_behavior}` - Formatted expected behaviors
- `{reporting_process}` - Reporting process
- `{contact_info}` - Contact information

### Staff SOPs (`staff_sops.md`)

- `{server_name}` - Server name
- `{staff_roles}` - List of staff roles (array)
- `{formatted_staff_roles}` - Formatted staff roles
- `{procedures}` - List of procedures (array)
- `{formatted_procedures}` - Formatted procedures
- `{escalation_path}` - Escalation path

### Moderation Guidelines (`moderation_guidelines.md`)

- `{server_name}` - Server name
- `{moderation_actions}` - List of moderation actions (array)
- `{formatted_moderation_actions}` - Formatted moderation actions
- `{warning_system}` - Warning system description
- `{ban_criteria}` - Ban criteria

### Appeal Process (`appeal_process.md`)

- `{server_name}` - Server name
- `{appeal_requirements}` - Appeal requirements
- `{review_process}` - Review process
- `{timelines}` - Timelines
- `{contact_info}` - Contact information

## Advanced Customization

### Adding Static Content

Add sections that don't change:

```markdown
# {server_name} - Server Rules

## Introduction

Welcome to our community! These rules help maintain a positive environment.

## Rules
{formatted_rules}

## Additional Information

- Our server is LGBTQ+ friendly
- We support multiple languages
- Events are held weekly on Fridays

## Contact
{contact_info}
```

### Using Markdown Formatting

Templates support full Markdown:

```markdown
# {server_name} Rules

> **Important:** Please read all rules before participating.

## 📜 Our Rules

{formatted_rules}

### ⚠️ Enforcement

{consequences}

---

**Need Help?** {contact_info}
```

### Conditional Content

While templates don't support conditionals directly, you can use placeholder text:

```markdown
{consequences}

*Note: For severe violations, immediate action may be taken without prior warnings.*
```

### Adding Images

You can reference images (users will need to add them manually):

```markdown
![Server Logo](path/to/logo.png)

# {server_name} Rules
```

## Template Best Practices

### 1. Keep It Readable

- Use clear headings
- Break content into sections
- Use lists and formatting appropriately

### 2. Include All Variables

- Don't remove required variables
- Add fallback text for optional variables
- Test with all form fields

### 3. Maintain Consistency

- Use consistent formatting across templates
- Match your server's tone and style
- Keep branding consistent

### 4. Test Thoroughly

- Generate documents after changes
- Check all variables are replaced
- Verify formatting looks correct

### 5. Version Control

- Keep templates in version control
- Document changes
- Create backups before major edits

## Example: Complete Custom Template

Here's a fully customized Server Rules template:

```markdown
# 🎮 {server_name} - Community Rules

Welcome to our amazing community! To ensure everyone has a great experience, please follow these guidelines.

---

## 📞 Contact & Support

**Need help?** {contact_info}

**Support Hours:** Monday-Friday, 9 AM - 5 PM EST

---

## 📋 Community Rules

{formatted_rules}

---

## ⚖️ Enforcement Policy

{consequences}

### Appeal Process

If you believe a moderation action was unfair, you can appeal by contacting our moderation team.

---

## 🎯 Our Values

- **Respect:** Treat everyone with kindness
- **Inclusion:** Everyone is welcome
- **Fun:** Let's have a great time together!

---

*These rules are subject to change. Members will be notified of significant updates.*

*Last Updated: [Date]*
*Version: 1.0*
```

## Troubleshooting Templates

### Variables Not Replacing

**Problem:** `{variable_name}` appears literally in generated document

**Solution:**
- Check variable name matches form data keys
- Verify template file encoding is UTF-8
- Ensure bot was restarted after template changes

### Formatting Issues

**Problem:** Generated document has poor formatting

**Solution:**
- Check Markdown syntax
- Verify list formatting
- Test with sample data

### Missing Content

**Problem:** Some content doesn't appear in generated document

**Solution:**
- Check all required variables are in template
- Verify form handler provides all data
- Review template for syntax errors

## Next Steps

- Learn about [Adding New Document Types](adding-documents.md)
- Check [API Reference](../api/reference.md) for programmatic access
- See [Troubleshooting](../troubleshooting.md) for common issues
