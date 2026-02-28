#!/usr/bin/env python3
"""
Check if tools.json is ordered alphabetically by the 'title' field.
"""
import json
import sys

def check_ordering(json_file):
    """
    Check if entries are ordered alphabetically by title field.
    
    Uses case-insensitive comparison to ensure consistent ordering
    regardless of capitalization (e.g., 'Abc' comes before 'xyz').
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print("ERROR: JSON root must be an array")
            return False
        
        # Check for missing titles and collect titles
        titles = []
        for i, entry in enumerate(data):
            if 'title' not in entry:
                print(f"ERROR: Entry at index {i} is missing required 'title' field")
                return False
            titles.append(entry['title'])
        
        # Sort titles case-insensitively for consistent ordering
        sorted_titles = sorted(titles, key=lambda x: x.lower())
        
        if titles != sorted_titles:
            print("ERROR: Tool entries are not ordered alphabetically by 'title' field")
            print("\nExpected order:")
            for i, (actual, expected) in enumerate(zip(titles, sorted_titles)):
                if actual != expected:
                    print(f"  Position {i}: Found '{actual}', expected '{expected}'")
            return False
        
        print("SUCCESS: All entries are ordered alphabetically by 'title' field")
        return True
    
    except FileNotFoundError:
        print(f"ERROR: File '{json_file}' not found")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON - {e}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_ordering.py <json_file>")
        sys.exit(1)
    
    success = check_ordering(sys.argv[1])
    sys.exit(0 if success else 1)
