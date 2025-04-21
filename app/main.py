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
    birth_date: datetime.date
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
    max_students = 0

    with open("groups.pickle", "wb") as groups_info:
        for group in groups:
            pickle.dump(group, groups_info)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(studs: list[Student]) -> int:
    with open("students.pickle", "wb") as students_info:
        for stud in studs:
            pickle.dump(stud, students_info)
    return len(studs)


def read_groups_information() -> list:
    groups = []

    with open("groups.pickle", "rb") as groups_info:
        while True:
            try:
                group = pickle.load(groups_info)
                if group.specialty.name not in groups:
                    groups.append(group.specialty.name)
            except EOFError:
                break
    return groups


def read_students_information() -> list[Student]:
    students = []

    with open("students.pickle", "rb") as students_info:
        while True:
            try:
                student = pickle.load(students_info)
                students.append(student)
            except EOFError:
                break
    return students
