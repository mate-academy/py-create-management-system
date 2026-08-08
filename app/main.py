from dataclasses import dataclass
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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    res = 0
    for group in groups:
        if len(group.students) > res:
            res = len(group.students)
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return res


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        info = pickle.load(file)
    return list(set([i.specialty.name for i in info]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        info = pickle.load(file)
    return info
