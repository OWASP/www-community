#!/usr/bin/env python3
"""
Check if tools.json is ordered alphabetically by the 'title' field.
"""
import json
import sys


def load_titles(json_file):
    """Load title strings from a tools JSON array. Raises on bad shape."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON root must be an array")

    titles = []
    for i, entry in enumerate(data):
        if 'title' not in entry:
            raise ValueError(f"Entry at index {i} is missing required 'title' field")
        titles.append(entry['title'])
    return titles


def correct_index(titles, index):
    """
    Index where titles[index] belongs under case-insensitive sort.

    Stable for duplicate titles: equals that currently appear earlier stay earlier.
    """
    key = titles[index].lower()
    smaller = sum(1 for title in titles if title.lower() < key)
    equal_before = sum(
        1 for j, title in enumerate(titles)
        if j < index and title.lower() == key
    )
    return smaller + equal_before


def format_move(titles, index):
    """One-line placement advice with current spot and correct neighbors."""
    title = titles[index]
    sorted_titles = sorted(titles, key=str.lower)
    # Prefer this occurrence when titles collide (stable by correct_index).
    sorted_at = correct_index(titles, index)
    before = sorted_titles[sorted_at - 1] if sorted_at > 0 else None
    after = (
        sorted_titles[sorted_at + 1]
        if sorted_at + 1 < len(sorted_titles)
        else None
    )

    if before and after:
        where = f"between '{before}' and '{after}'"
    elif after:
        where = f"before '{after}' (start of list)"
    else:
        where = f"after '{before}' (end of list)"

    if index > 0:
        currently = f"currently after '{titles[index - 1]}'"
    else:
        currently = "currently at start of list"

    return (
        f"ERROR: Move '{title}' (index {index}, {currently}) to {where}"
    )


def indices_to_advise(titles, base_titles=None):
    """
    Pick entries that should be reported as moves.

    Prefer titles absent from base (typical PR add). Otherwise report only
    entries with maximum displacement so a late insert does not blame every
    shifted neighbor (cascade noise from zip-vs-sorted).
    """
    wrong = [
        i for i in range(len(titles))
        if i != correct_index(titles, i)
    ]
    if not wrong:
        return []

    if base_titles is not None:
        base_keys = {title.lower() for title in base_titles}
        added_wrong = [
            i for i in wrong
            if titles[i].lower() not in base_keys
        ]
        if added_wrong:
            return added_wrong

    max_displacement = max(abs(i - correct_index(titles, i)) for i in wrong)
    return [
        i for i in wrong
        if abs(i - correct_index(titles, i)) == max_displacement
    ]


def check_ordering(json_file, base_file=None):
    """
    Check if entries are ordered alphabetically by title field.

    Uses case-insensitive comparison. On failure, prints where to move
    misplaced entries (not adjacent-swap hints).
    """
    try:
        titles = load_titles(json_file)

        base_titles = None
        if base_file:
            try:
                base_titles = load_titles(base_file)
            except (OSError, ValueError, json.JSONDecodeError) as e:
                print(f"WARNING: Could not load base file '{base_file}': {e}")
                print("Falling back to displacement-only placement advice.")
                print("")

        advise = indices_to_advise(titles, base_titles)
        if not advise:
            print(
                "SUCCESS: All entries are ordered alphabetically by 'title' field"
            )
            return True

        print(
            "ERROR: Tool entries are not ordered alphabetically by "
            "'title' (case-insensitive)."
        )
        print("")
        for index in advise:
            print(format_move(titles, index))
        return False

    except FileNotFoundError:
        print(f"ERROR: File '{json_file}' not found")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON - {e}")
        return False
    except ValueError as e:
        print(f"ERROR: {e}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: check_ordering.py <json_file> [base_json_file]")
        sys.exit(1)

    base = sys.argv[2] if len(sys.argv) == 3 else None
    success = check_ordering(sys.argv[1], base)
    sys.exit(0 if success else 1)
