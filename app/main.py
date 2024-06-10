import pickle

from datetime import datetime
from dataclasses import dataclass
from typing import List


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: Group) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    max_student = max(len(group.students) for group in groups)
    return max_student


def write_students_information(students: Student) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

        for group in groups:
            specialties.add(group.specialty.name)

    return list(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)

        return students
