import pickle
from typing import List
from app.Group import Group
from app.Student import Student
from app.Specialty import Specialty


def write_groups_information(groups : List[Group]) -> int:

    with open("groups.pickle", "wb") as pickle_file:

        for group in groups:
            pickle.dump(group, pickle_file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:

        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> set:

    groups = []
    with open("groups.pickle", "rb") as file:

        while True:
            try:
                groups.append(pickle.load(file))
            except EOFError:
                break

    return set(group.specialty.name for group in groups)


def read_students_information() -> List:

    students = []
    with open("students.pickle", "rb") as file:

        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break

    return students
