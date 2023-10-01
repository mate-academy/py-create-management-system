import dataclasses
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
    student: List[Student]


def write_group_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students = max(len(group.student) for group in groups)
    return max_students


def write_students_information(student: List[Student]) -> int:
    with open("students_pickle", "wb") as file:
        pickle.dump(student, file)
        number_of_student = len(student)
    return number_of_student


def read_group_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialities = set()
    for group in groups:
        specialities.add(group.specialty.name)
    return specialities


def read_student_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
