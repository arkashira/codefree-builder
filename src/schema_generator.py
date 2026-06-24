from dataclasses import dataclass
from json import JSONDecodeError
from typing import Any
from .schema_validator import SchemaValidator  # Import SchemaValidator

@dataclass
class SchemaGeneratorConfig:
    schema_validator: SchemaValidator

class SchemaGenerator:
    def __init__(self, config: SchemaGeneratorConfig):
        self.config = config

    def generate_schema(self, schema: Any) -> str:
        try:
            self.config.schema_validator.validate(schema)  # Simplistic schema generation for demonstration purposes
            return "CREATE TABLE table_name (\n" + "\n".join([f"{key} VARCHAR(255)" for key in schema.keys()]) + "\n);"
        except ValueError as e:
            raise ValueError(f"Invalid schema: {e}")
