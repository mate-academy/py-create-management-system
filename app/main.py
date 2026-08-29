from __future__ import annotations

import pickle
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max_students


def write_students_information(students: list[Student]) -> int:
    students_count = len(students)

    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return students_count


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    unique_specialty_names = set(group.specialty.name for group in groups)

    return list(unique_specialty_names)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
