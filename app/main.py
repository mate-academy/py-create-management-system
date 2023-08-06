from __future__ import annotations

import pickle
from dataclasses import dataclass
from datetime import date

from app.constants import (GROUP_PICKL, STUDENTS_PICKL)
from app.pickle_data import get_pickle_data


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    students = []
    with open(GROUP_PICKL, "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
            for student in group.students:
                if student not in students:
                    students.append(student)
    return len(students)


def write_students_information(students: list[Student]) -> int:
    with open(STUDENTS_PICKL, "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information(file_name: str = GROUP_PICKL) -> list:
    specialties = []
    for group in get_pickle_data(file_name):
        specialties.append(group.specialty.name)
    return list(dict.fromkeys(specialties))


def read_students_information(file_name: str = STUDENTS_PICKL) -> list[Student]:
    output = []
    for student in get_pickle_data(file_name):
        if student not in output:
            output.append(student)
    return output
