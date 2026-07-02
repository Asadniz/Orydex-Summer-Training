"""
Task 1 — Slicing and Loops

Practice slicing, loops, enumerate, zip, and comprehensions.
Complete this file without using AI tools.
"""

patient_ids = [101, 102, 103, 104, 105, 106, 107]
patient_names = ["Ayesha", "Omar", "Sara", "Bilal", "Hina", "Usman", "Maha"]

from helper import uppercase

def slicing_examples():
    """Return examples of list slicing."""
    # TODO: Return first three IDs, last three IDs, and reversed IDs.
    new_lst = [patient_ids[0:3], patient_ids[-3:], patient_ids[::-1]]
    print ("Slicing: ", new_lst)
    return new_lst


def loop_examples():
    """Practice range, enumerate, and zip."""
    # TODO: Use enumerate to print numbered patient names.
    # TODO: Use zip to pair IDs with names.
    enum = enumerate(patient_names)
    id_name_pairs = zip(range(len(patient_ids)), patient_ids, patient_names)
    print ("Enumerate: ", list(enum))
    print ("Zip: ", list(id_name_pairs))
    return(enum, id_name_pairs)


def comprehension_examples():
    """Return values created using comprehensions."""
    # TODO: Create a list of even patient IDs.
    # TODO: Create uppercase patient names.
    even_patient_ids = [x for x in patient_ids if x % 2 == 0]
    uppercase_names = [uppercase(x) for x in patient_names]
    print("Even patient IDs: ", even_patient_ids)
    print("Uppercase names", uppercase_names)
    return (even_patient_ids, uppercase_names)


if __name__ == "__main__":
    slicing_examples()
    loop_examples()
    comprehension_examples()
