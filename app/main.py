from __future__ import annotations
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
    course: str
    students: list[Student]


def write_groups_information(group_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_info, file)
    max_student = [len(group.students) for group in group_info]
    return 0 if group_info == [] else max(max_student)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        specialty_names = {group.specialty.name for group in pickle.load(file)}
    return list(specialty_names)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        student_list = [student for student in pickle.load(file)]
    return student_list
