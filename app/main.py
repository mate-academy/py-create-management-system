from __future__ import annotations
from dataclasses import dataclass

import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_information: list[Group]) -> int:

    with open("groups.pickle", "wb") as groups:
        pickle.dump(group_information, groups)

    groups_students = []

    for group in group_information:
        groups_students.append(len(group.students))

    return max(groups_students) if groups_students else 0


def write_students_information(students_information: list[Student]) -> int:

    with open("students.pickle", "wb") as students:
        pickle.dump(students_information, students)

    return len(students_information)


def read_groups_information() -> set:

    with open("groups.pickle", "rb") as groups:
        groups_info = pickle.load(groups)

    return set([group.specialty.name for group in groups_info])


def read_students_information() -> list[Student]:

    with open("students.pickle", "rb") as students:
        students_info = pickle.load(students)

    return students_info
