from __future__ import annotations

import pickle
from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open("groups.pickle", "wb") as gr:
        pickle.dump(groups, gr)

    return max(
        (
            len(group.students)
            for group in groups
            if group.students
        ), default=0
    )


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as st:
        pickle.dump(students, st)

    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as gr:
        groups = pickle.load(gr)

        return set([group.specialty.name for group in groups])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as st:
        return pickle.load(st)
