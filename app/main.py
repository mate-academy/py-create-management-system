import dataclasses
import pickle

from datetime import datetime
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
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    name_of_speciality = []
    for group in groups:
        name_of_speciality.append(group.specialty.name)
    name_of_speciality = set(name_of_speciality)
    return name_of_speciality


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
