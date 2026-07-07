"""
Task 1 — Collection Operations

Practice lists, tuples, and sets.
Complete this file without using AI tools.
"""

# Sample data — do not edit.
sample_conditions = ["diabetes", "asthma", "hypertension"]
primary_conditions = {"diabetes", "asthma", "hypertension"}
follow_up_conditions = {"asthma", "cardiac", "diabetes"}


def list_operations(conditions: list[str]) -> list[str]:
    """Return a new, sorted list after adding and removing a condition.

    Steps:
    - Work on a copy so the input list is not modified.
    - Add "cardiac".
    - Remove "asthma".
    - Return the list sorted alphabetically.
    """
    # TODO: Implement the steps described above.
    pass


def set_operations(primary: set[str], follow_up: set[str]) -> dict[str, set[str]]:
    """Return common, all-unique, and primary-only conditions.

    Return a dictionary with these keys:
    - "common": conditions in both sets
    - "all_unique": every condition across both sets
    - "only_primary": conditions in primary but not in follow_up
    """
    # TODO: Build and return the dictionary described above.
    pass


if __name__ == "__main__":
    print(list_operations(sample_conditions))
    print(set_operations(primary_conditions, follow_up_conditions))
