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
    birth_date: datetime(2021, 2, 25)
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
    return max([len(user.students) for user in groups], default=0)


def write_students_information(student: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(student, pickle_file)
    return len(student)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        student = pickle.load(pickle_file)
        return set([user.specialty.name for user in student])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        student = pickle.load(pickle_file)
        return student
