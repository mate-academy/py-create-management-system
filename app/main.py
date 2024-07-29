import pickle

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: str


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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_info:
        groups = pickle.load(groups_info)
    specialities = {group.specialty.name for group in groups}
    return list(specialities)


def read_students_information() -> list:
    with open("students.pickle", "rb") as students:
        students_instances = pickle.load(students)
    return list(student for student in students_instances)
