import pickle
from dataclasses import dataclass
from datetime import datetime
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
    students: List[Student]


def write_groups_information(group_lists: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_lists, file)
    if group_lists:
        return max(len(group.students) for group in group_lists)


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
        return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        group = pickle.load(file)
        return set([name.specialty.name for name in group])


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_info = pickle.load(file)
        return students_info
