"""
Task 1 — Patient Summary

Complete this file without using AI tools.
Use fake/sample data only.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "condition": "diabetes", "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "condition": "hypertension", "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "condition": "asthma", "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "condition": "diabetes", "active": True},
]

from helper import b_sort


def total_patients(patient_records):
    """Return the total number of patients."""
    # TODO: Implement this function.
    count = 0
    for patient in patient_records:
        count += 1
    return count


def average_age(patient_records):
    """Return the average patient age."""
    # TODO: Implement this function.
    age_sum = 0
    for patient in patient_records:
        age_sum += patient["age"]
    return (age_sum/total_patients(patient_records))


def count_active_patients(patient_records):
    """Return the number of active patients."""
    # TODO: Implement this function.
    count = 0
    for patient in patient_records:
        if patient["active"]:
            count += 1
    return count


def unique_conditions(patient_records):
    """Return a sorted list of unique conditions."""
    # TODO: Implement this function.
    lst = []
    for patient in patient_records:
        if patient["condition"] not in lst:
            lst.append(patient["condition"])

    b_sort(lst)

    return lst


def count_by_condition(patient_records):
    """Return a dictionary containing patient count by condition."""
    # TODO: Implement this function.
    patients_by_condition = {}
    for patient in patient_records:
        count = 1
        for temp in patient_records:
            if patient["id"] != temp["id"] and patient["condition"] == temp["condition"]:
                count += 1
        patients_by_condition[patient["condition"]] = count
    return patients_by_condition



if __name__ == "__main__":
    # TODO: Print the summary results clearly.
    print ("SUMMARY")
    print ("----------")
    print ("Patients: ")
    
    for patient in patients:
        print (patient)

    print ("Total patients: ", total_patients(patients))
    print ("Average Age: ", average_age(patients))
    print ("Active Patients: ", count_active_patients(patients))
    print ("Unique Conditions: ", unique_conditions(patients))
    print ("Patients by Conditions: ", count_by_condition(patients))
    print ("----------")