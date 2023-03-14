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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    students = [0]
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    for group in groups:
        students.append(len(group.students))
    return max(students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set[str]:
    specialties = set()
    with open("groups.pickle", "rb") as read_groups_file:
        groups = pickle.load(read_groups_file)
        for group in groups:
            specialties.add(group.specialty.name)
    specialties = list(specialties)
    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as read_students_file:
        student = pickle.load(read_students_file)
    return student
