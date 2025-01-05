from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import Any


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
        if not groups:
            return 0
        max_students = max(len(group.students) for group in groups)
        return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        students_number = 0
        for student in students:
            students_number += 1
        return students_number


def read_groups_information() -> Any:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specialities = set()

    for group in groups:
        specialities.add(group.specialty.name)

    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    students_list = []
    for student in students:
        students_list.append(student)
    return students_list
