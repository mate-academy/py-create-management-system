import pickle

from datetime import datetime
from dataclasses import dataclass


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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    students_count = 0
    for group in groups:
        if students_count < len(group.students):
            students_count = len(group.students)
    with open("groups.pickle", "wb") as groups_pickle_file:
        pickle.dump(groups, groups_pickle_file)
    return students_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle_file:
        pickle.dump(students, students_pickle_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    return set(group.specialty.name for group in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students_information = pickle.load(f)
    return [students for students in students_information]
