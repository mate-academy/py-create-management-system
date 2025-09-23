import pickle
from dataclasses import dataclass
from datetime import datetime
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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as g:
        pickle.dump(groups, g)
    if groups:
        return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as s:
        pickle.dump(students, s)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as g:
        groups = pickle.load(g)
        return set(group_s.specialty.name for group_s in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as s:
        return pickle.load(s)
