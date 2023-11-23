from dataclasses import dataclass
from datetime import datetime
from typing import List
from pickle import dump, load


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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        dump(groups, f)

    if len(groups):
        return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        dump(students, f)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        return list(set(group.specialty.name for group in load(f)))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        return load(f)
