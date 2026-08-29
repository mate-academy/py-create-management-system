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
    students: list


def write_groups_information(groups: list[Group] | None = None) -> int:
    if groups is None:
        groups = []
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student] | None = None) -> int:
    if students is None:
        students = []
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> set[str]:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
                students.append(student)
            except EOFError:
                break
    return students
