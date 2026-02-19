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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int | None:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)
    if group_list:
        return max(len(i.students) for i in group_list)
    return None


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student_list, file)
    return len(student_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups_info = pickle.load(file)
    return set(group.specialty.name for group in groups_info)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        student_list = pickle.load(file)
    return [student for student in student_list]
