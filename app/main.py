from dataclasses import dataclass
from datetime import datetime
import pickle
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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: List[Group]) -> int:

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if len(groups) != 0:
        return max([len(group.students) for group in groups])
    return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        info = pickle.load(file)
    return list(set(group.specialty.name for group in info))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        info = pickle.load(file)
    return info
