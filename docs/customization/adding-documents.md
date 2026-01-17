# Adding New Document Types

Learn how to add custom document types to the bot.

## Overview

Adding a new document type requires:

1. Creating a template file
2. Adding the document type to configuration
3. Creating a form handler
4. Testing the new document type

## Step 1: Create Template File

Create a new Markdown template in `bot/templates/`:

```bash
bot/templates/my_document_type.md
```

### Template Structure

Use placeholder variables that will be replaced with form data:

```markdown
# {server_name} - My Custom Document

## Introduction

{introduction_text}

## Main Content

{main_content}

## Contact

{contact_info}
```

## Step 2: Update Configuration

Add your document type to `config/config.py`:

```python
DOCUMENT_TYPES = {
    "rules": "Server Rules",
    "privacy_policy": "Privacy Policy",
    # ... existing types ...
    "my_document_type": "My Custom Document",  # Add your new type
}
```

The key (e.g., `"my_document_type"`) must match your template filename (without `.md`).

## Step 3: Create Form Handler

Add a modal form handler in `bot/handlers/form_handler.py`.

### Step 3a: Add Modal Method

Add a method to create your document's modal:

```python
def _get_my_document_modal(self) -> discord.ui.Modal:
    """Modal for My Custom Document."""
    server_name = discord.ui.TextInput(
        label="Server Name",
        placeholder="Enter your server name",
        required=True,
        max_length=100
    )
    
    introduction_text = discord.ui.TextInput(
        label="Introduction Text",
        placeholder="Enter introduction",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=500
    )
    
    main_content = discord.ui.TextInput(
        label="Main Content",
        placeholder="Enter main content",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=2000
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
            "introduction_text": introduction_text.value,
            "main_content": main_content.value,
            "contact_info": contact_info.value or "Contact server administrators"
        }
        await self._process_form(interaction, "my_document_type", form_data)
    
    modal = DynamicModal(title="Generate My Custom Document", callback_func=callback)
    modal.add_item(server_name)
    modal.add_item(introduction_text)
    modal.add_item(main_content)
    modal.add_item(contact_info)
    return modal
```

### Step 3b: Register the Modal

Update the `_get_form_modal` method to include your new document type:

```python
def _get_form_modal(self, document_type: str) -> discord.ui.Modal:
    """Get the appropriate modal form for a document type."""
    modals = {
        "rules": self._get_rules_modal,
        "privacy_policy": self._get_privacy_policy_modal,
        # ... existing modals ...
        "my_document_type": self._get_my_document_modal,  # Add your modal
    }
    
    return modals.get(document_type, self._get_generic_modal)()
```

### Step 3c: Update Document Type Display

Update the `get_document_type_embed` method to include your new type:

```python
def get_document_type_embed(self) -> discord.Embed:
    """Create an embed for document type selection."""
    # ... existing code ...
    
    document_types = {
        "rules": "📋 Server Rules",
        # ... existing types ...
        "my_document_type": "📄 My Custom Document",  # Add your type
    }
    
    # ... rest of method ...
```

Update `DocumentTypeView` in the same file:

```python
document_types = [
    ("rules", "📋 Rules"),
    # ... existing types ...
    ("my_document_type", "📄 Custom"),  # Add your type
]
```

## Step 4: Test Your New Document Type

1. **Restart the bot**
2. **Test the command:**
   ```
   /generate my_document_type
   ```
3. **Fill out the form** and verify the generated document
4. **Check the template** variables are replaced correctly

## Complete Example

Here's a complete example of adding a "Community Guidelines" document type:

### 1. Template File (`bot/templates/community_guidelines.md`)

```markdown
# {server_name} - Community Guidelines

## Welcome

{welcome_message}

## Guidelines

{guidelines}

## Enforcement

{enforcement_policy}

## Contact

{contact_info}
```

### 2. Configuration (`config/config.py`)

```python
DOCUMENT_TYPES = {
    # ... existing types ...
    "community_guidelines": "Community Guidelines",
}
```

### 3. Form Handler (`bot/handlers/form_handler.py`)

```python
def _get_community_guidelines_modal(self) -> discord.ui.Modal:
    """Modal for Community Guidelines."""
    server_name = discord.ui.TextInput(
        label="Server Name",
        placeholder="Enter your server name",
        required=True,
        max_length=100
    )
    
    welcome_message = discord.ui.TextInput(
        label="Welcome Message",
        placeholder="Welcome message for new members",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=500
    )
    
    guidelines = discord.ui.TextInput(
        label="Guidelines (one per line)",
        placeholder="Guideline 1\nGuideline 2\nGuideline 3",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=1500
    )
    
    enforcement_policy = discord.ui.TextInput(
        label="Enforcement Policy",
        placeholder="How guidelines are enforced",
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
            "welcome_message": welcome_message.value,
            "guidelines": [g.strip() for g in guidelines.value.split("\n") if g.strip()],
            "enforcement_policy": enforcement_policy.value,
            "contact_info": contact_info.value or "Contact server administrators"
        }
        await self._process_form(interaction, "community_guidelines", form_data)
    
    modal = DynamicModal(title="Generate Community Guidelines", callback_func=callback)
    modal.add_item(server_name)
    modal.add_item(welcome_message)
    modal.add_item(guidelines)
    modal.add_item(enforcement_policy)
    modal.add_item(contact_info)
    return modal
```

Update the modal registry:

```python
modals = {
    # ... existing modals ...
    "community_guidelines": self._get_community_guidelines_modal,
}
```

## Handling Lists in Templates

If your form collects list data (like rules or guidelines), the `DocumentGenerator` automatically formats them. In your template, use:

```markdown
{guidelines}  # Raw list (array)
```

Or format manually in the template:

```markdown
## Guidelines

{formatted_guidelines}
```

The generator converts arrays to formatted markdown lists automatically.

## Best Practices

### 1. Naming Conventions

- Use snake_case for document type keys: `my_document_type`
- Use descriptive names: `community_guidelines` not `doc1`
- Match template filename to document type key

### 2. Form Design

- Keep forms concise (Discord modals have limits)
- Use appropriate input types (short vs paragraph)
- Mark required fields clearly
- Provide helpful placeholders

### 3. Template Design

- Use clear section headings
- Include all form variables
- Provide fallback text for optional fields
- Test with various input lengths

### 4. Error Handling

The existing `_process_form` method handles errors, but you can add custom validation:

```python
async def callback(interaction: discord.Interaction):
    # Custom validation
    if len(guidelines.value.split("\n")) < 3:
        await interaction.response.send_message(
            "Please provide at least 3 guidelines.",
            ephemeral=True
        )
        return
    
    form_data = {
        # ... form data ...
    }
    await self._process_form(interaction, "document_type", form_data)
```

## Troubleshooting

### Document Type Not Appearing

**Problem:** New document type doesn't show in selection menu

**Solution:**
- Verify it's in `DOCUMENT_TYPES` dictionary
- Check `get_document_type_embed` includes it
- Ensure `DocumentTypeView` has the button
- Restart the bot

### Form Not Showing

**Problem:** Modal doesn't appear when selecting document type

**Solution:**
- Check modal is registered in `_get_form_modal`
- Verify method name matches
- Check for syntax errors in modal method
- Review bot logs for errors

### Variables Not Replacing

**Problem:** Template variables appear literally

**Solution:**
- Ensure form data keys match template variables
- Check variable names are exact (case-sensitive)
- Verify template file encoding

### Template Not Found

**Problem:** Error says template file not found

**Solution:**
- Verify template file exists in `bot/templates/`
- Check filename matches document type key
- Ensure file has `.md` extension
- Check file permissions

## Next Steps

- Learn about [Template Customization](templates.md)
- Check [API Reference](../api/reference.md) for advanced usage
- See [Troubleshooting](../troubleshooting.md) for help
