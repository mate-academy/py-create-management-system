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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if groups:
        number_of_students = []
        for group in groups:
            number_of_students.append(len(group.students))
        return int(max(number_of_students))


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
        return len(students)


def read_groups_information() -> list:
    specialities = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        for group in groups:
            specialities.append(group.specialty.name)
    return list(set(specialities))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
        return students
