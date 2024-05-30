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
    course: int
    students: Student


def write_groups_information(groups: list) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
        pickle.dump(groups, file)

    return max_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    specialities = []
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        for group in groups:
            if group.specialty.name not in specialities:
                specialities.append(group.specialty.name)
    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
