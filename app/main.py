from dataclasses import dataclass
import pickle
from typing import List
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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = 0
    for group in groups:
        if max_students < len(group.students):
            max_students = len(group.students)

    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialty = [group.specialty.name for group in groups]
    return set(specialty)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
