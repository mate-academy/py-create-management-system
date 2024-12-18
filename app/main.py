import pickle
from typing import List
from app.Group import Group
from app.Student import Student


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students = 0
    for group in groups:
        if max_students < len(group.students):
            max_students = len(group.students)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialties = {group.specialty.name for group in groups}
    return specialties


def read_students_information() -> set:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
