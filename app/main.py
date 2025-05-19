from datetime import datetime
import pickle
from dataclasses import dataclass


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
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_students_information() -> list:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                students.append(pickle.load(f))
    except EOFError:
        pass
    return students


def read_groups_information() -> list:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                group = pickle.load(f)
                specialties.add(group.specialty.name)
    except EOFError:
        pass
    return list(specialties)
