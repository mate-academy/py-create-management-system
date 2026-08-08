import pickle

from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
