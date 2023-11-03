from dataclasses import dataclass
from datetime import datetime
from typing import List
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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    count_student = 0
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    for group in groups:
        if len(group.students) > count_student:
            count_student = len(group.students)
    return count_student


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    list_groups = []
    for group in groups:
        list_groups.append(group.specialty.name)
    return set(list_groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
