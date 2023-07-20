import dataclasses
import pickle
from datetime import datetime
from typing import Any


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
    students: list


def write_groups_information(groups: dict) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: dict) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialties = set()
    for group in groups:
        specialties.add(group.specialty.name)

    return list(specialties)


def read_students_information() -> Any:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
