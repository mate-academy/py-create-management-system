import dataclasses
import pickle
from datetime import datetime
from typing import List


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
    max_students = 0

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialties = []
    for group in groups:
        if group.specialty.name not in specialties:
            specialties.append(group.specialty.name)

    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
