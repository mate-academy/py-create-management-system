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


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_list, file)

    if groups_list:
        return max([len(group.students) for group in groups_list])
    return 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)

    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        list_groups = pickle.load(file)

    return list(set([group.specialty.name for group in list_groups]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        list_students = pickle.load(file)

    return list_students
