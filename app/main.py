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


def write_groups_information(
    liceum_groups: list[Group]
) -> int:
    max_students_in_group = 0

    with open("groups.pickle", "wb") as file:
        for group in liceum_groups:
            if max_students_in_group < len(group.students):
                max_students_in_group = len(group.students)
            pickle.dump(group, file)

    return max_students_in_group


def write_students_information(
    students: list[Student]
) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list[Group]:
    specialties = []
    groups = []

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                single_group = pickle.load(file)
                groups.append(single_group)
            except EOFError:
                break

    for group in groups:
        if group.specialty.name not in specialties:
            specialties.append(group.specialty.name)

    return specialties


def read_students_information() -> list[Student]:
    students = []

    with open("students.pickle", "rb") as file:

        while True:
            try:
                single_student = pickle.load(file)
                students.append(single_student)
            except EOFError:
                break

    return students
