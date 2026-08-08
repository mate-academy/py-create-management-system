import dataclasses
import pickle

from typing import List
from datetime import datetime


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


def write_groups_information(groups: Group) -> int:
    with open("groups.pickle", "wb") as write_groups:
        pickle.dump(groups, write_groups)
    max_student = max([len(group.students) for group in groups], default=-1)
    return max_student


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as write_students:
        pickle.dump(students, write_students)
    return len(students)


def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as read_groups:
            groups = pickle.load(read_groups)
    except FileNotFoundError:
        groups = []
    unique_specialty = set()
    for group in groups:
        unique_specialty.add(group.specialty.name)
    return list(unique_specialty)


def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as read_students:
            all_students = pickle.load(read_students)
    except FileNotFoundError:
        all_students = []
    return all_students
