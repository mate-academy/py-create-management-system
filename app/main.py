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
    course: int
    students: list[Student]


def write_groups_information(group_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_info, file)
        max_value = 0
        for group in group_info:
            if len(group.students) > max_value:
                max_value = len(group.students)
    return max_value


def write_students_information(students_info: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students_info:
            pickle.dump(student, file)
    return len(students_info)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    return set(group.specialty.name for group in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        all_students = []
        while True:
            try:
                all_students.append(pickle.load(file))
            except EOFError:
                break
    return all_students
