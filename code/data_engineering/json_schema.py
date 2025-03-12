# Import necessary modules
import json
from jsonschema import validate

# Define the JSON Schema
schema_definition = {
    "$schema": "http://json-schema.org/draft-07/schema#",  # JSON Schema version
    "type": "object",  # Root must be an object
    # Define properties of the root object
    "properties": {
        "nombre": {"type": "string"},  # Must be a string
        "edad": {"type": "integer", "minimum": 0},  # Must be a non-negative integer
        "es_estudiante": {"type": "boolean"},  # Must be a boolean
        "habilidades": {
            "type": "array",  # Must be an array
            "items": {"type": "string"},  # Each item must be a string
            "minItems": 1,  # At least one item required
            "uniqueItems": True,  # All items must be unique
        },
        "direccion": {
            "type": "object",  # Must be an object
            "properties": {
                "calle": {"type": "string"},  # Must be a string
                "ciudad": {"type": "string"},  # Must be a string
                "codigo_postal": {
                    "type": "string",
                    "pattern": "^[0-9]{5}$",
                },  # Must be 5 digits
            },
            "required": [
                "calle",
                "ciudad",
                "codigo_postal",
            ],  # These fields are mandatory
        },
    },
    # Root object must have these fields
    "required": ["nombre", "edad", "es_estudiante", "habilidades", "direccion"],
}

# Path to the JSON file
json_file_path = (
    r"D:\Proyectos de codigo\python\code\data_sources\Json_data\student.json"
)

# Load the JSON file
with open(json_file_path, "r", encoding="utf-8") as file:
    json_data = json.load(file)

# Validate the JSON against the schema
try:
    validate(instance=json_data, schema=schema_definition)
    print("The JSON is valid.")
except Exception as err:
    print("The JSON is invalid:", err)
