from __future__ import annotations

from dataclasses import dataclass
import pickle
from datetime import datetime


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
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)

    return (
        0
        if not len(groups)
        else max((len(group.students) for group in groups))
    )


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)

    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        return pickle.load(students_file)
