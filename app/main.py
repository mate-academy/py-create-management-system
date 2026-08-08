import dataclasses
import os
from builtins import int
from datetime import datetime
import pickle
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        return 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(student: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student, file)
        number_of_student = len(student)
    return number_of_student


def read_groups_information() -> set:
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
        specialities = set()
        for group in groups:
            specialities.add(group.specialty.name)
        return specialities
    else:
        return set()


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
