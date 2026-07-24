import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[str]:
    specialty_names = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
            except EOFError:
                break
            if group.specialty.name not in specialty_names:
                specialty_names.append(group.specialty.name)
    return specialty_names


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
            except EOFError:
                break
            students.append(student)
    return students
