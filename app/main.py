import dataclasses
from datetime import datetime
import pickle
from typing import Any


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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            pickle.dump(group, pickle_file)
    max_student = max([len(group.students) for group in group_list], default=0)
    return max_student


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_list:
            pickle.dump(student, pickle_file)

    return len(student_list)


def read_groups_information() -> list[Any]:
    groups = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                groups.append(group)
            except EOFError:
                break
    unique_spec = {group.specialty.name for group in groups}
    return list(unique_spec)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students.append(student)
            except EOFError:
                break
    return students
