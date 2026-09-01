from dataclasses import dataclass
import pickle
from datetime import datetime
from typing import Any


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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        for group in groups:
            pickle.dump(group, group_file)
    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
    return len(students)


def read_groups_information(group_file: Any = "groups.pickle") -> list:
    groups = []
    with open(group_file, "rb") as file:
        while True:
            try:
                groups.append(pickle.load(file))
            except EOFError:
                break
        return sorted(set(group.specialty.name for group in groups))


def read_students_information(
        student_file: Any = "students.pickle"
) -> list[Student]:
    students = []
    with open(student_file, "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break
        return students
