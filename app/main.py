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
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)

    max_students = 0
    if groups:
        max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)

    return len(students)


def read_groups_information() -> list:
    specialties = set()

    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        if isinstance(groups, Group):
            groups = [groups]
        for group in groups:
            specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> list:

    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)

    if isinstance(students, Student):
        students = [students]
    return students
