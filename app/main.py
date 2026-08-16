from __future__ import annotations
from dataclasses import dataclass, field
import pickle
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student] = field(default_factory=list)


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)

    return len(students)


def read_groups_information() -> list[str]:
    specialties: set[str] = set()

    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:
                group = pickle.load(groups_file)
            except EOFError:
                break

            specialties.add(group.specialty.name)

    return list(specialties)


def read_students_information() -> list[Student]:
    students: list[Student] = []

    with open("students.pickle", "rb") as students_file:
        while True:
            try:
                student = pickle.load(students_file)
            except EOFError:
                break

            students.append(student)

    return students
