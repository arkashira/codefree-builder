from dataclasses import dataclass
from typing import Any

@dataclass
class SchemaValidatorConfig:
    required_properties: list[str]

class SchemaValidator:
    def __init__(self, config: SchemaValidatorConfig):
        self.config = config

    def validate(self, schema: Any) -> None:
        if not isinstance(schema, dict):
            raise ValueError("Invalid schema type. Expected a dictionary.")
        for property in self.config.required_properties:
            if property not in schema:
                raise ValueError(f"Missing required property: {property}")
