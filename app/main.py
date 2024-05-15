from dataclasses import dataclass
import pickle
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
    average_mark: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students) + 1


def read_groups_information(file_name: str) -> set:
    with open(file_name, "rb") as file:
        groups = pickle.load(file)
    return {group.specialty.name for group in groups}


def read_students_information(file_name: str) -> list:
    with open(file_name, "rb") as file:
        students = pickle.load(file)
    return students

