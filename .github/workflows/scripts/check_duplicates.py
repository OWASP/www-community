#!/usr/bin/env python3
"""
Check if tools.json contains duplicate entries.
Detects duplicates by:
- Title (case-insensitive, normalized)
- URL (normalized - trailing slashes removed)

Normalization helps detect similar entries like:
- "FindSecBugs" vs "Find Security Bugs"
- "https://example.com/" vs "https://example.com"
"""
import json
import sys
import re
from collections import defaultdict


def normalize_title(title):
    """
    Normalize title for duplicate detection.
    - Convert to lowercase
    - Remove spaces, hyphens, underscores
    - Remove special characters
    
    This helps detect titles like:
    - "FindSecBugs" vs "Find Security Bugs"
    - "PVS-Studio" vs "PVSStudio"
    """
    if not title:
        return ""
    # Convert to lowercase and remove spaces, hyphens, underscores
    normalized = title.lower()
    normalized = re.sub(r'[\s\-_]', '', normalized)
    # Remove other special characters except alphanumeric
    normalized = re.sub(r'[^a-z0-9]', '', normalized)
    return normalized


def normalize_url(url):
    """
    Normalize URL for duplicate detection.
    - Remove trailing slashes
    - Convert to lowercase (domain is case-insensitive)
    
    This helps detect URLs like:
    - "https://example.com/" vs "https://example.com"
    """
    if not url:
        return ""
    # Remove trailing slash
    normalized = url.rstrip('/')
    return normalized


def check_duplicates(json_file):
    """
    Check if entries have duplicate titles or URLs.
    Uses normalized comparison to catch similar entries.
    
    Returns True if no duplicates found, False otherwise.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print("ERROR: JSON root must be an array")
            return False
        
        # Track duplicates using normalized keys
        # Map: normalized_key -> [(index, original_value), ...]
        normalized_titles_map = defaultdict(list)
        normalized_urls_map = defaultdict(list)
        has_duplicates = False
        
        # Collect all titles and URLs with their indices
        for i, entry in enumerate(data):
            if 'title' in entry:
                title = entry['title']
                normalized = normalize_title(title)
                normalized_titles_map[normalized].append((i, title))
            if 'url' in entry:
                url = entry['url']
                normalized = normalize_url(url)
                normalized_urls_map[normalized].append((i, url))
        
        # Check for duplicate titles (normalized)
        duplicate_titles = {norm: entries for norm, entries in normalized_titles_map.items() if len(entries) > 1}
        if duplicate_titles:
            print("ERROR: Found duplicate titles (case-insensitive, normalized)\n")
            for normalized, entries in sorted(duplicate_titles.items()):
                # Group by original title to show if they're exact matches or variations
                original_titles = set(title for _, title in entries)
                if len(original_titles) == 1:
                    print(f"Exact duplicate title '{entries[0][1]}' appears {len(entries)} times:")
                else:
                    titles_list = ', '.join(f"'{title}'" for _, title in entries)
                    print(f"Similar titles detected (normalized: '{normalized}'):")
                    print(f"  Variations: {titles_list}")
                
                for idx, original_title in entries:
                    entry = data[idx]
                    print(f"  Entry #{idx}: '{original_title}'")
                    print(f"    URL: {entry.get('url', 'N/A')}")
                    print(f"    Owner: {entry.get('owner', 'N/A')}")
                    print(f"    License: {entry.get('license', 'N/A')}")
                print()
            has_duplicates = True
        
        # Check for duplicate URLs (normalized)
        duplicate_urls = {norm: entries for norm, entries in normalized_urls_map.items() if len(entries) > 1}
        if duplicate_urls:
            print("ERROR: Found duplicate URLs (normalized - trailing slashes removed)\n")
            for normalized, entries in sorted(duplicate_urls.items()):
                # Check if all URLs are exactly the same or just normalized-same
                original_urls = set(url for _, url in entries)
                if len(original_urls) == 1:
                    print(f"Exact duplicate URL '{entries[0][1]}' appears {len(entries)} times:")
                else:
                    urls_list = ', '.join(f"'{url}'" for _, url in entries)
                    print(f"Similar URLs detected (differ only in trailing slashes):")
                    print(f"  Variations: {urls_list}")
                
                for idx, original_url in entries:
                    entry = data[idx]
                    print(f"  Entry #{idx}: '{entry.get('title', 'N/A')}'")
                    print(f"    URL: {original_url}")
                    print(f"    Owner: {entry.get('owner', 'N/A')}")
                    print(f"    License: {entry.get('license', 'N/A')}")
                print()
            has_duplicates = True
        
        if has_duplicates:
            print(f"SUMMARY: Found {len(duplicate_titles)} duplicate title group(s) and {len(duplicate_urls)} duplicate URL group(s)")
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
