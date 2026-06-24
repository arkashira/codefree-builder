from schema_generator import SchemaGenerator
from api_generator import ApiGenerator
from schema_validator import SchemaValidator, SchemaValidatorConfig

def main():
    schema = {
        "table_name": {
            "column1": "",
            "column2": ""
        }
    }
    schema_validator_config = SchemaValidatorConfig(required_properties=["column1", "column2"])
    schema_generator_config = SchemaGenerator.SchemaGeneratorConfig(schema_validator=SchemaValidator(schema_validator_config))
    api_generator_config = ApiGenerator.ApiGeneratorConfig(schema=schema)
    schema_generator = SchemaGenerator(schema_generator_config)
    api_generator = ApiGenerator(api_generator_config)
    print(schema_generator.generate_schema(schema["table_name"]))  # Pass the inner dictionary
    print(api_generator.generate_api())

if __name__ == "__main__":
    main()
