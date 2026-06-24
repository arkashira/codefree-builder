import pytest
from src.schema_generator import SchemaGenerator, SchemaGeneratorConfig
from src.schema_validator import SchemaValidator, SchemaValidatorConfig

def test_schema_generator_valid_schema():
    config = SchemaGeneratorConfig(schema_validator=SchemaValidator(SchemaValidatorConfig(required_properties=["column1", "column2"])))
    generator = SchemaGenerator(config)
    schema = {"column1": "", "column2": ""}
    generated_schema = generator.generate_schema(schema)
    assert "CREATE TABLE table_name (" in generated_schema

def test_schema_generator_invalid_schema_missing_property():
    config = SchemaGeneratorConfig(schema_validator=SchemaValidator(SchemaValidatorConfig(required_properties=["column1", "column2"])))
    generator = SchemaGenerator(config)
    schema = {"column1": ""}
    with pytest.raises(ValueError):
        generator.generate_schema(schema)

def test_schema_generator_invalid_schema_invalid_type():
    config = SchemaGeneratorConfig(schema_validator=SchemaValidator(SchemaValidatorConfig(required_properties=["column1", "column2"])))
    generator = SchemaGenerator(config)
    schema = "invalid schema"
    with pytest.raises(ValueError):
        generator.generate_schema(schema)
