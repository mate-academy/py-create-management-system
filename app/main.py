import os
import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import Any


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    if groups:
        with open("groups.pickle", "wb") as f:
            pickle.dump(groups, f)
        return max(len(group.students) for group in groups)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set[Any] | list[Any]:
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
            specialities = [group.specialty.name for group in groups]
        return set(specialities)
    return []


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        students = [student for student in students]
    return students
