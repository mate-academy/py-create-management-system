from __future__ import annotations

import pickle
import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:

    with open("groups.pickle", "wb") as output:
        pickle.dump(groups, output)

    return max(len(group.students) for group in groups) if groups else []


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as output:
        pickle.dump(students, output)

    return len(students)


def read_groups_information() -> list:

    with open("groups.pickle", "rb") as file:
        data = pickle.load(file)

    return list(set(group.specialty.name for group in data))


def read_students_information() -> list[Student]:

    with open("students.pickle", "rb") as file:
        data = pickle.load(file)

    return data
