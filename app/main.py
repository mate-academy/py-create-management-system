from dataclasses import dataclass
from datetime import datetime
from typing import Set
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
    specialty: list[Specialty]
    course: int
    students: list[Student]


# = datetime.now().year

def write_groups_information(groups: list[Group]) -> int:
    max_val = 0
    with open("groups.pickle", "wb") as gr:
        for group in groups:
            pickle.dump(group, gr)
            if len(group.students) > max_val:
                max_val = len(group.students)
    return max_val


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as st:
        for student in students:
            pickle.dump(student, st)
    return len(students)


def read_groups_information() -> set[str]:
    specialties: Set[str] = set()
    with open("groups.pickle", "rb") as gr:
        while True:
            try:
                group = pickle.load(gr)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as st:
        while True:
            try:
                student = pickle.load(st)
                students.append(student)
            except EOFError:
                break
    return students
