from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime
import pickle


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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        if os.path.getsize("groups.pickle") > 0:
            return list(
                set(group.specialty.name for group in pickle.load(file))
            )


def read_students_information() -> int:
    with open("students.pickle", "rb") as file:
        if os.path.getsize("students.pickle") > 0:
            return pickle.load(file)
