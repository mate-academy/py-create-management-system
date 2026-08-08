import pickle
from dataclasses import dataclass
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
    with open("groups.pickle", "wb") as groups_info:
        for group in groups:
            pickle.dump(group, groups_info)

    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_info:
        for student in students:
            pickle.dump(student, students_info)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_info:
        groups = []
        while True:
            try:
                group = pickle.load(groups_info)
                groups.append(group)
            except EOFError:
                break

    return list({group.specialty.name: None for group in groups}.keys())


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_info:
        students = []
        while True:
            try:
                student = pickle.load(students_info)
                students.append(student)
            except EOFError:
                break

    return students
