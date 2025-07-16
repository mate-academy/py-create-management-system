from dataclasses import dataclass
from datetime import datetime
import pickle
import os


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(info: list[Group]) -> int:
    if not info:
        return 0

    with open("groups.pickle", "wb") as file:
        pickle.dump(info, file)

    return max(len(group.students) for group in info)


def write_students_information(student: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student, file)

    return len(student)


def read_groups_information() -> set:
    if not os.path.exists("groups.pickle"):
        return set()

    with open("groups.pickle", "rb") as file:
        names = pickle.load(file)

    return set(group.specialty.name for group in names)


def read_students_information() -> list:
    if not os.path.exists("students.pickle"):
        return []

    with open("students.pickle", "rb") as file:
        names = list(pickle.load(file))

    return names
