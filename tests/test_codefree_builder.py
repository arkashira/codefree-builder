import pytest
import json
from codefree_builder import CodeFreeBuilder, Template, Theme

def test_add_template():
    builder = CodeFreeBuilder()
    template = Template("Test Template", ["header", "footer"])
    builder.add_template(template)
    assert len(builder.get_templates()) == 1

def test_add_theme():
    builder = CodeFreeBuilder()
    theme = Theme("Test Theme", ["red", "blue"])
    builder.add_theme(theme)
    assert len(builder.get_themes()) == 1

def test_customize_layout():
    builder = CodeFreeBuilder()
    template = Template("Test Template", ["header", "footer"])
    builder.add_template(template)
    components = ["header", "content", "footer"]
    customized_template = builder.customize_layout("Test Template", components)
    assert customized_template.layout == components

def test_customize_design():
    builder = CodeFreeBuilder()
    theme = Theme("Test Theme", ["red", "blue"])
    builder.add_theme(theme)
    colors = ["green", "yellow"]
    customized_theme = builder.customize_design("Test Theme", colors)
    assert customized_theme.colors == colors

def test_save_design():
    builder = CodeFreeBuilder()
    template = Template("Test Template", ["header", "footer"])
    theme = Theme("Test Theme", ["red", "blue"])
    builder.add_template(template)
    builder.add_theme(theme)
    design = builder.save_design(template, theme)
    assert json.loads(design) == {
        "template": "Test Template",
        "layout": ["header", "footer"],
        "theme": "Test Theme",
        "colors": ["red", "blue"]
    }

def test_template_not_found():
    builder = CodeFreeBuilder()
    with pytest.raises(ValueError):
        builder.customize_layout("Non Existent Template", ["header", "footer"])

def test_theme_not_found():
    builder = CodeFreeBuilder()
    with pytest.raises(ValueError):
        builder.customize_design("Non Existent Theme", ["red", "blue"])
