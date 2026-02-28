#!/usr/bin/env python3
"""
Check if tools.json conforms to the JSON schema.
Uses Python's jsonschema library for validation with user-friendly error messages.
"""
import json
import sys
from jsonschema import Draft7Validator, FormatChecker


def check_schema(schema_file, json_file):
    """Check if JSON file conforms to the schema."""
    try:
        # Load schema
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        
        # Load data
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Create validator with format checking (for URIs, dates, etc.)
        validator = Draft7Validator(schema, format_checker=FormatChecker())
        
        # Collect all validation errors
        errors = list(validator.iter_errors(data))
        
        if errors:
            print(f"ERROR: Schema validation failed with {len(errors)} error(s)\n")
            
            for i, error in enumerate(errors, 1):
                # Get the path to the error (e.g., which entry)
                path_list = list(error.path)
                
                if path_list:
                    entry_index = path_list[0]
                    field_path = " -> ".join(str(p) for p in path_list[1:]) if len(path_list) > 1 else None
                    
                    # Try to get the entry title for better context
                    try:
                        entry_title = data[entry_index].get('title', 'Unknown')
                        print(f"Entry #{entry_index} ('{entry_title}'):")
                    except (IndexError, AttributeError, TypeError):
                        print(f"Entry #{entry_index}:")
                    
                    print(f"  Error: {error.message}")
                    if field_path:
                        print(f"  Field: {field_path}")
                else:
                    print(f"Error {i}: {error.message}")
                
                # Show validator type for additional context
                if error.validator in ['required', 'enum', 'minimum', 'maximum', 'format']:
                    if error.validator == 'required':
                        print(f"  Required fields: {error.validator_value}")
                    elif error.validator == 'enum':
                        print(f"  Allowed values: {error.validator_value}")
                    elif error.validator in ['minimum', 'maximum']:
                        print(f"  Constraint: {error.validator} = {error.validator_value}")
                    elif error.validator == 'format':
                        print(f"  Expected format: {error.validator_value}")
                
                print()
            
            return False
        
        print("SUCCESS: All entries conform to the schema")
        return True
    
    except FileNotFoundError as e:
        print(f"ERROR: File not found - {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON - {e}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: check_schema.py <schema_file> <json_file>")
        sys.exit(1)
    
    success = check_schema(sys.argv[1], sys.argv[2])
    sys.exit(0 if success else 1)
