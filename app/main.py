import pickle
from dataclasses import dataclass
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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_len = 0
    for group in groups:
        max_len = max(max_len, len(group.students))
    return max_len


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties_names = set()
    for group in groups:
        specialties_names.add(group.specialty.name)
    return specialties_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
