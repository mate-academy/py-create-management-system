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
    max_group = 0
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
        for group in groups:
            if len(group.students) > max_group:
                max_group = len(group.students)
    return max_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> list:
    specialties = []
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
    for group in groups:
        if group.specialty.name not in specialties:
            specialties.append(group.specialty.name)
    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return students
