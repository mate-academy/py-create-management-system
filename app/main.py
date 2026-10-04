import os
import pickle

from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: int | float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

        for group in groups:
            max_students = max(max_students, len(group.students))

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> list[str]:
    specialty_names = []

    if os.path.isfile("groups.pickle"):
        with open("groups.pickle", "rb") as pickle_file:
            groups = pickle.load(pickle_file)

            for group in groups:
                specialty_names.append(group.specialty.name)

    return list(set(specialty_names))


def read_students_information() -> list[Student]:
    students = []
    if os.path.isfile("students.pickle"):
        with open("students.pickle", "rb") as pickle_file:
            students = pickle.load(pickle_file)

    return students
