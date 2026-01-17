"""Document generator that processes templates and replaces variables."""

import os
from pathlib import Path
from typing import Dict, Any
from config.config import TEMPLATES_DIR


class DocumentGenerator:
    """Handles template loading and document generation."""
    
    def __init__(self):
        self.templates_dir = Path(TEMPLATES_DIR)
    
    def load_template(self, document_type: str) -> str:
        """Load a template file for the given document type."""
        template_path = self.templates_dir / f"{document_type}.md"
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")
        
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    
    def generate_document(self, document_type: str, variables: Dict[str, Any]) -> str:
        """
        Generate a document by replacing template variables.
        
        Args:
            document_type: Type of document to generate
            variables: Dictionary of variable names and values to substitute
        
        Returns:
            Generated markdown document as string
        """
        template = self.load_template(document_type)
        
        # Replace all variables in the template
        # Handle both {variable} and {variable_name} formats
        document = template
        
        for key, value in variables.items():
            # Replace {key} and {key_name} patterns
            placeholder = f"{{{key}}}"
            if placeholder in document:
                # Convert value to string, handle lists and None
                if value is None:
                    str_value = "N/A"
                elif isinstance(value, list):
                    str_value = "\n".join(f"- {item}" for item in value) if value else "None"
                else:
                    str_value = str(value)
                document = document.replace(placeholder, str_value)
        
        # Clean up any remaining placeholders
        import re
        document = re.sub(r'\{[^}]+\}', 'N/A', document)
        
        return document
    
    def get_available_document_types(self) -> list:
        """Get list of available document types based on template files."""
        if not self.templates_dir.exists():
            return []
        
        return [
            f.stem for f in self.templates_dir.glob("*.md")
            if f.is_file()
        ]
