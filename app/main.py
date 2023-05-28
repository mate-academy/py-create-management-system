import pickle
import dataclasses
from datetime import datetime
from typing import List


@dataclasses
class Specialty:
    name: str
    number: int


@dataclasses
class Student:
    first_name: str
    lase_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses
class Group:
    specialty: Specialty
    course: int
    student: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if groups:
        return max(len(group.students) for group in groups)
    return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        return set(group.specialty.name for group in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
