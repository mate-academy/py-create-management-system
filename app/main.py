import pickle
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
    birth_date: type[datetime]
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
    biggest_group = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    for group in groups:
        if len(group.students) > biggest_group:
            biggest_group = len(group.students)
    return biggest_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return {group.specialty.name for group in groups}


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
