import pickle

from app.group import Group
from app.specialty import Specialty
from app.student import Student


def write_groups_information(lyceum_groups: list[Group]) -> int:
    maximum_number_of_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in lyceum_groups:
            if len(group.students) > maximum_number_of_students:
                maximum_number_of_students = len(group.students)
            pickle.dump(group, pickle_file)
    return maximum_number_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list:
    file_path = "groups.pickle"
    groups: Specialty.name = []
    try:
        with open(file_path, "rb") as file:
            while True:
                try:
                    group = pickle.load(file)
                    groups.append(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return list(set(groups))


def read_students_information() -> list:
    students = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                try:
                    student = pickle.load(file)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return students
