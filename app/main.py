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


def write_groups_information(list_group: list[Group]) -> int:

    with open("groups.pickle", "wb") as groups:
        pickle.dump(list_group, groups)

    if not list_group:
        return 0

    return max(len(group.students) for group in list_group)


def write_students_information(list_student: list[Student]) -> int:

    with open("students.pickle", "wb") as students:
        pickle.dump(list_student, students)

    return len(list_student)


def read_groups_information() -> list[str]:

    with open("groups.pickle", "rb") as file:
        list_groups = pickle.load(file)

    if not list_groups:
        return []

    return list({group.specialty.name for group in list_groups})


def read_students_information() -> list[Student]:

    with open("students.pickle", "rb") as file:
        file_students = pickle.load(file)

    return file_students
