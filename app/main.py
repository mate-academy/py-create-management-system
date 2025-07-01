from dataclasses import dataclass
from datetime import datetime
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
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    max_len = 0
    for group in group_list:
        if len(group.students) > max_len:
            max_len = len(group.students)
    return max_len


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        group_list = pickle.load(f)
    return list(set([group.specialty.name for group in group_list]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)
    return students_list
