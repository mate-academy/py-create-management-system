import pickle
from dataclasses import dataclass
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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students_number = 0
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    for group in groups:
        if max_students_number < len(group.students):
            max_students_number = len(group.students)
    return max_students_number


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    all_specialties = []
    for group in groups:
        if group.specialty.name not in all_specialties:
            all_specialties.append(group.specialty.name)
    return all_specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    all_students = []
    for student in students:
        all_students.append(student)
    return all_students
