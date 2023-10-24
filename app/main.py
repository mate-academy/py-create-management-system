import pickle

from typing import List
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
    course: int | str
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    students_count = []
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    for group in groups:
        students_count.append(len(group.students))
    return max(students_count) if students_count else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return set([group.specialty.name for group in groups])


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
