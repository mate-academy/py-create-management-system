import dataclasses
from datetime import datetime
from typing import List
import pickle


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


def write_groups_information(list_of_groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)

    max_number = 0

    for group in list_of_groups:
        if len(group.students) > max_number:
            max_number = len(group.students)

    return max_number


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)

    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    name_of_speciality = []

    for group in groups:
        name_of_speciality.append(group.specialty.name)

    name_of_speciality = set(name_of_speciality)

    return name_of_speciality


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        list_of_students = pickle.load(f)

    return list_of_students
