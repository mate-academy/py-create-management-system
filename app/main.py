from __future__ import annotations

import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    result = 0
    if not groups:
        return 0
    for group in groups:
        if result < len(group.students):
            result = len(group.students)
    return result


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        result = []

        for group in groups:
            if group.specialty.name not in result:
                result.append(group.specialty.name)

        return result


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)

        return students
