import pickle
from dataclasses import dataclass
from datetime import date
from typing import List


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_number_of_students = max(
        [len(group.students) for group in groups]
    ) if len(groups) > 0 else 0
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max_number_of_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialties = list(set(group.specialty.name for group in groups))
    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    students = [student for student in students]
    return students
