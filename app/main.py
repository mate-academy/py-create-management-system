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


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_students_information() -> list[Student]:
    students_info = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                students_info.append(pickle.load(file))
            except EOFError:
                break
    return students_info


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    return max((len(group.students) for group in groups), default=0)


def read_groups_information() -> set[str]:
    specialties_names = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialties_names.add(group.specialty.name)
            except EOFError:
                break
    return specialties_names
