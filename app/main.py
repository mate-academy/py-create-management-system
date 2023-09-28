from __future__ import annotations
from datetime import datetime
from typing import List

import dataclasses
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    students_number = 0
    for group in groups:
        if len(group.students) > students_number:
            students_number += len(group.students)
    return students_number


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    specialities = []
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        for group in groups:
            if group.specialty.name not in specialities:
                specialities.append(group.specialty.name)
    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
