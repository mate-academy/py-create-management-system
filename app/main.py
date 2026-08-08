from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass
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
    course: int | datetime
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students_count = 0

    with open("groups.pickle", "wb") as pickle_file:

        for group in groups:
            pickle.dump(group, pickle_file)

            if len(group.students) > max_students_count:
                max_students_count = len(group.students)

    return max_students_count


def write_students_information(students: list[Group]) -> int:
    students_count = 0

    with open("students.pickle", "wb") as pickle_file:

        for student in students:
            students_count += 1
            pickle.dump(student, pickle_file)

    return students_count


def read_groups_information() -> set:
    specialty_names = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialty_names.add(group.specialty.name)
            except EOFError:
                return specialty_names


def read_students_information() -> None:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students.append(student)
            except EOFError:
                return students
