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


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0

    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
                specialties.add(group.specialty.name)
            except EOFError:
                return specialties


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                students.append(pickle.load(f))

            except EOFError:
                return students
