from dataclasses import dataclass
import pickle
from datetime import datetime


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
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> set:
    speciality = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                group = pickle.load(f)
                speciality.add(group.specialty.name)
    except EOFError:
        pass
    return speciality


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                student = pickle.load(f)
                students.append(student)
    except EOFError:
        pass
    return students
