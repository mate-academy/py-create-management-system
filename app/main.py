from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List


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
    students: List[Student]


def write_groups_information(lyceum_groups: List[Group]) -> int:

    with open("groups.pickle", "wb") as file:
        pickle.dump(lyceum_groups, file)
        max_number = 0

    for group in lyceum_groups:
        if len(group.students) > max_number:
            max_number = len(group.students)

    return max_number


def write_students_information(students: List[Student]) -> int:

    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set:

    specialties = []

    with open("groups.pickle", "rb") as file:
        lyceum_group = pickle.load(file)

    for group in lyceum_group:
        specialties.append(group.specialty.name)

    return set(specialties)


def read_students_information() -> list:

    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
