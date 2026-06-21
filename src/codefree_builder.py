import json
from dataclasses import dataclass
from typing import List

@dataclass
class Template:
    name: str
    layout: List[str]

@dataclass
class Theme:
    name: str
    colors: List[str]

class CodeFreeBuilder:
    def __init__(self):
        self.templates = []
        self.themes = []

    def add_template(self, template: Template):
        self.templates.append(template)

    def add_theme(self, theme: Theme):
        self.themes.append(theme)

    def get_templates(self):
        return self.templates

    def get_themes(self):
        return self.themes

    def customize_layout(self, template_name: str, components: List[str]):
        template = next((t for t in self.templates if t.name == template_name), None)
        if template:
            template.layout = components
            return template
        else:
            raise ValueError("Template not found")

    def customize_design(self, theme_name: str, colors: List[str]):
        theme = next((t for t in self.themes if t.name == theme_name), None)
        if theme:
            theme.colors = colors
            return theme
        else:
            raise ValueError("Theme not found")

    def save_design(self, template: Template, theme: Theme):
        design = {
            "template": template.name,
            "layout": template.layout,
            "theme": theme.name,
            "colors": theme.colors
        }
        return json.dumps(design)
