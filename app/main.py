from datetime import datetime
from typing import List
import dataclasses
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
        correct_info = pickle.load(file)

    return set(group.specialty.name for group in correct_info)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        correct_info = pickle.load(file)

    return correct_info
