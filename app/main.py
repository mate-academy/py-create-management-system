from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
import pickle


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
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_from_pickle(file_name: str) -> list[Student]:
    with open(file_name, "rb") as pickle_file:
        items = pickle.load(pickle_file)
        return items


def read_groups_information(file_name: str = "groups.pickle") -> set:
    groups = read_from_pickle(file_name)
    return set(group.specialty.name for group in groups)


def read_students_information(
        file_name: str = "students.pickle"
) -> list[Student]:
    students = read_from_pickle(file_name)
    return students
