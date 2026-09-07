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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    students_list = []

    for group in groups:
        for student in group.students:
            if student not in students_list:
                students_list.append(student)

    return len(students_list)


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> list[str]:

    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

    specialties = set(group.specialty.name for group in groups)
    return list(specialties)


def read_students_information() -> list[Student]:

    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)

    return students
