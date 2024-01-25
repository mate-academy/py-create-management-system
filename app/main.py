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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_group:
        for group in groups:
            pickle.dump(group, pickle_group)

    if not groups:
        return 0
    return max([len(group.students) for group in groups])


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        for student in students:
            pickle.dump(student, pickle_students)

    return len(students)


def read_groups_information() -> list[str]:
    specialties = set()
    with open("groups.pickle", "rb") as pickle_group:
        try:
            while True:
                group = pickle.load(pickle_group)
                specialties.add(group.specialty.name)
        except EOFError:
            pass

    return list(specialties)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as pickle_students:
        try:
            while True:
                student = pickle.load(pickle_students)
                students.append(student)
        except EOFError:
            pass

    return students
