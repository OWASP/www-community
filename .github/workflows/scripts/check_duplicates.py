#!/usr/bin/env python3
"""
Check if tools.json contains duplicate entries.
Detects duplicates by:
- Title (exact match, case-sensitive)
- URL (exact match)
"""
import json
import sys
from collections import defaultdict


def check_duplicates(json_file):
    """
    Check if entries have duplicate titles or URLs.
    
    Returns True if no duplicates found, False otherwise.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print("ERROR: JSON root must be an array")
            return False
        
        # Track duplicates
        titles_map = defaultdict(list)
        urls_map = defaultdict(list)
        has_duplicates = False
        
        # Collect all titles and URLs with their indices
        for i, entry in enumerate(data):
            if 'title' in entry:
                titles_map[entry['title']].append(i)
            if 'url' in entry:
                urls_map[entry['url']].append(i)
        
        # Check for duplicate titles
        duplicate_titles = {title: indices for title, indices in titles_map.items() if len(indices) > 1}
        if duplicate_titles:
            print("ERROR: Found duplicate titles\n")
            for title, indices in sorted(duplicate_titles.items()):
                print(f"Title '{title}' appears {len(indices)} times:")
                for idx in indices:
                    entry = data[idx]
                    print(f"  Entry #{idx}:")
                    print(f"    URL: {entry.get('url', 'N/A')}")
                    print(f"    Owner: {entry.get('owner', 'N/A')}")
                    print(f"    License: {entry.get('license', 'N/A')}")
                print()
            has_duplicates = True
        
        # Check for duplicate URLs
        duplicate_urls = {url: indices for url, indices in urls_map.items() if len(indices) > 1}
        if duplicate_urls:
            print("ERROR: Found duplicate URLs\n")
            for url, indices in sorted(duplicate_urls.items()):
                print(f"URL '{url}' appears {len(indices)} times:")
                for idx in indices:
                    entry = data[idx]
                    print(f"  Entry #{idx}: '{entry.get('title', 'N/A')}'")
                    print(f"    Owner: {entry.get('owner', 'N/A')}")
                    print(f"    License: {entry.get('license', 'N/A')}")
                print()
            has_duplicates = True
        
        if has_duplicates:
            print(f"SUMMARY: Found {len(duplicate_titles)} duplicate title(s) and {len(duplicate_urls)} duplicate URL(s)")
            return False
        
        print("SUCCESS: No duplicate titles or URLs found")
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
        print("Usage: check_duplicates.py <json_file>")
        sys.exit(1)
    
    success = check_duplicates(sys.argv[1])
    sys.exit(0 if success else 1)
