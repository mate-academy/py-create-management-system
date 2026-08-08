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


def write_groups_information(groups_list: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_list, f)
    max_students = 0
    for group in groups_list:
        if max_students < len(group.students):
            max_students = len(group.students)
    return max_students


def write_students_information(students_list: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups_list = pickle.load(f)
    return set([group.specialty.name for group in groups_list])


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)
    return students_list
