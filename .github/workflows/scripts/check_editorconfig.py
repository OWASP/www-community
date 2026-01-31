#!/usr/bin/env python3
"""
Check if tools.json adheres to .editorconfig rules.
Rules for *.json files:
- indent_style = tab
- indent_size = 1
- charset = utf-8
- end_of_line = lf
- insert_final_newline = true
- trim_trailing_whitespace = true
"""
import sys
import json
import re


def check_json_structural_indentation(text, lines):
    """
    Check if JSON structural indentation adheres to tab-based rules.
    Validates that braces, brackets, and their contents are properly indented.
    Uses JSON structure to identify which entry errors belong to.
    """
    errors = []
    
    # Try to parse JSON to get entry information
    try:
        data = json.loads(text)
        is_array = isinstance(data, list)
    except json.JSONDecodeError as e:
        errors.append(f"ERROR: Invalid JSON - {e}")
        return errors
    
    # Track expected indentation depth and current entry
    depth = 0
    in_string = False
    escape_next = False
    current_entry_index = None
    current_entry_title = None
    
    for i, line in enumerate(lines, 1):
        # Skip the final empty line
        if i == len(lines) and line == '':
            continue
        
        stripped = line.strip()
        
        # Skip empty lines
        if not stripped:
            continue
        
        # Track which entry we're in based on depth
        # At depth 1, we're inside a top-level array entry
        if is_array and depth == 1:
            # Check if this line starts a new entry (opening brace at depth 1)
            if stripped == '{' or stripped.startswith('{'):
                # We're entering a new entry - count how many entries we've seen
                # by counting previous opening braces at this depth
                entry_count = 0
                for prev_i in range(i - 1, 0, -1):
                    prev_line = lines[prev_i - 1].strip()
                    # Count opening braces that would be at depth 1
                    if len(lines[prev_i - 1]) > 0 and lines[prev_i - 1][0] == '\t':
                        if not lines[prev_i - 1].startswith('\t\t'):
                            if prev_line == '{' or prev_line.startswith('{'):
                                entry_count += 1
                
                current_entry_index = entry_count
                if current_entry_index < len(data):
                    current_entry_title = data[current_entry_index].get('title')
        elif depth == 0:
            # Outside of any entry
            current_entry_index = None
            current_entry_title = None
        
        # Count leading tabs and check for mixed indentation
        leading_tabs = 0
        has_mixed_indentation = False
        for j, char in enumerate(line):
            if char == '\t':
                leading_tabs += 1
            elif char == ' ':
                # Found space in indentation area - this is an error
                if current_entry_index is not None and current_entry_title:
                    errors.append(
                        f"ERROR: Entry #{current_entry_index} ('{current_entry_title}'): Line {i} has space character in indentation "
                        f"(position {j+1}): tabs and spaces should not be mixed"
                    )
                elif current_entry_index is not None:
                    errors.append(
                        f"ERROR: Entry #{current_entry_index}: Line {i} has space character in indentation "
                        f"(position {j+1}): tabs and spaces should not be mixed"
                    )
                else:
                    errors.append(
                        f"ERROR: Line {i} has space character in indentation "
                        f"(position {j+1}): tabs and spaces should not be mixed"
                    )
                has_mixed_indentation = True
                break
            else:
                # First non-whitespace character
                break
        
        # Determine expected indentation based on the line content
        # Lines that decrease depth (closing braces/brackets)
        if stripped.startswith('}') or stripped.startswith(']'):
            expected_depth = depth - 1
        else:
            expected_depth = depth
        
        # Guard against negative depth (malformed JSON structure)
        if expected_depth < 0:
            expected_depth = 0
        
        # Check if indentation matches expected depth (skip if mixed indentation already reported)
        if not has_mixed_indentation and leading_tabs != expected_depth:
            # Get context for error message
            context = stripped[:50] + '...' if len(stripped) > 50 else stripped
            
            # Use entry information from structural tracking
            if current_entry_index is not None and current_entry_title:
                errors.append(
                    f"ERROR: Entry #{current_entry_index} ('{current_entry_title}'): Line {i} has incorrect indentation: "
                    f"expected {expected_depth} tab(s), found {leading_tabs} tab(s) - '{context}'"
                )
            elif current_entry_index is not None:
                errors.append(
                    f"ERROR: Entry #{current_entry_index}: Line {i} has incorrect indentation: "
                    f"expected {expected_depth} tab(s), found {leading_tabs} tab(s) - '{context}'"
                )
            else:
                errors.append(
                    f"ERROR: Line {i} has incorrect indentation: "
                    f"expected {expected_depth} tab(s), found {leading_tabs} tab(s) - '{context}'"
                )
        
        # Update depth for next line based on what's on this line
        # We need to properly count braces/brackets, ignoring those in strings
        line_in_string = in_string
        line_escape_next = escape_next
        open_count = 0
        close_count = 0
        
        for char in stripped:
            if line_escape_next:
                line_escape_next = False
                continue
            
            if char == '\\':
                line_escape_next = True
                continue
            
            if char == '"':
                line_in_string = not line_in_string
                continue
            
            if not line_in_string:
                if char == '{' or char == '[':
                    open_count += 1
                elif char == '}' or char == ']':
                    close_count += 1
        
        # Update the persistent string state for multi-line string support
        in_string = line_in_string
        escape_next = line_escape_next
        
        # Account for same-line open/close (like "[]" or "{}")
        net_change = open_count - close_count
        depth += net_change
        
        # Guard against negative depth
        if depth < 0:
            depth = 0
    
    return errors


def check_unicode_escapes(text, data):
    """
    Check if JSON file contains unnecessary Unicode escape sequences.
    Characters like ç, ê, etc. should be stored as-is, not as \u00e7, \u00ea.
    This requires ensure_ascii=False when using json.dump().
    """
    errors = []
    
    # Common Unicode escape patterns for Latin characters with diacritics (U+0000 to U+00FF)
    # These should be written directly, not escaped
    # Note: Using \\u00XX pattern to specifically target Latin-1 characters
    # which are commonly unnecessarily escaped (e.g., \\u00e7 for ç)
    unicode_escape_pattern = re.compile(r'\\u00[0-9a-fA-F]{2}')
    
    # Find all Unicode escape sequences - only proceed if any are found
    if not unicode_escape_pattern.search(text):
        return errors
    
    # Try to identify which entries contain these escapes
    if isinstance(data, list):
        for entry_index, entry in enumerate(data):
            entry_title = entry.get('title', 'Unknown')
            # Find specific fields with escapes
            fields_with_escapes = []
            for key, value in entry.items():
                if isinstance(value, str):
                    # Only serialize to check for escapes if the value might contain them
                    value_json = json.dumps(value, ensure_ascii=True)
                    if unicode_escape_pattern.search(value_json):
                        fields_with_escapes.append(key)
            
            if fields_with_escapes:
                errors.append(
                    f"ERROR: Entry #{entry_index} ('{entry_title}'): "
                    f"Contains Unicode escape sequences in field(s): {', '.join(fields_with_escapes)}. "
                    f"Use ensure_ascii=False in json.dump() to preserve special characters."
                )
    
    return errors


def check_editorconfig(json_file):
    """Check if JSON file adheres to .editorconfig rules."""
    errors = []
    
    try:
        with open(json_file, 'rb') as f:
            content = f.read()
        
        # Check charset (UTF-8)
        try:
            text = content.decode('utf-8')
        except UnicodeDecodeError:
            errors.append("ERROR: File is not UTF-8 encoded")
            print('\n'.join(errors))
            return False
        
        # Check end_of_line (LF)
        if b'\r\n' in content:
            errors.append("ERROR: File contains CRLF line endings (should be LF)")
        elif b'\r' in content:
            errors.append("ERROR: File contains CR line endings (should be LF)")
        
        # Check insert_final_newline
        if not content.endswith(b'\n'):
            errors.append("ERROR: File does not end with a newline")
        
        # Check trim_trailing_whitespace and indent_style (tabs)
        lines = text.split('\n')
        
        # Parse JSON to get entry information for error messages
        try:
            data = json.loads(text)
            is_array = isinstance(data, list)
        except (json.JSONDecodeError, Exception):
            data = None
            is_array = False
        
        # Track current entry while checking each line
        depth = 0
        current_entry_index = None
        current_entry_title = None
        
        for i, line in enumerate(lines, 1):
            # Skip the final empty line (result of file ending with \n)
            if i == len(lines) and line == '':
                continue
            
            stripped = line.strip()
            
            # Track which entry we're in based on depth (similar to structural check)
            if is_array and data and depth == 1:
                if stripped == '{' or stripped.startswith('{'):
                    # Count entries seen so far
                    entry_count = 0
                    for prev_i in range(i - 1, 0, -1):
                        prev_line = lines[prev_i - 1].strip()
                        if len(lines[prev_i - 1]) > 0 and lines[prev_i - 1][0] == '\t':
                            if not lines[prev_i - 1].startswith('\t\t'):
                                if prev_line == '{' or prev_line.startswith('{'):
                                    entry_count += 1
                    current_entry_index = entry_count
                    if current_entry_index < len(data):
                        current_entry_title = data[current_entry_index].get('title')
            elif depth == 0:
                current_entry_index = None
                current_entry_title = None
            
            # Check trailing whitespace
            if line.rstrip() != line:
                if current_entry_index is not None and current_entry_title:
                    errors.append(f"ERROR: Entry #{current_entry_index} ('{current_entry_title}'): Line {i} has trailing whitespace")
                elif current_entry_index is not None:
                    errors.append(f"ERROR: Entry #{current_entry_index}: Line {i} has trailing whitespace")
                else:
                    errors.append(f"ERROR: Line {i} has trailing whitespace")
            
            # Check for spaces used for indentation (should be tabs)
            if line.startswith(' '):
                if current_entry_index is not None and current_entry_title:
                    errors.append(f"ERROR: Entry #{current_entry_index} ('{current_entry_title}'): Line {i} uses spaces for indentation (should use tabs)")
                elif current_entry_index is not None:
                    errors.append(f"ERROR: Entry #{current_entry_index}: Line {i} uses spaces for indentation (should use tabs)")
                else:
                    errors.append(f"ERROR: Line {i} uses spaces for indentation (should use tabs)")
            
            # Update depth for entry tracking
            if not stripped:
                continue
            open_count = stripped.count('{') + stripped.count('[')
            close_count = stripped.count('}') + stripped.count(']')
            depth += (open_count - close_count)
            if depth < 0:
                depth = 0
        
        # Check JSON structural indentation
        structural_errors = check_json_structural_indentation(text, lines)
        errors.extend(structural_errors)
        
        # Check for Unicode escape sequences (if JSON is valid)
        if data is not None:
            unicode_errors = check_unicode_escapes(text, data)
            errors.extend(unicode_errors)
        
        if errors:
            print('\n'.join(errors))
            return False
        
        print("SUCCESS: File adheres to .editorconfig rules")
        return True
    
    except FileNotFoundError:
        print(f"ERROR: File '{json_file}' not found")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_editorconfig.py <json_file>")
        sys.exit(1)
    
    success = check_editorconfig(sys.argv[1])
    sys.exit(0 if success else 1)
