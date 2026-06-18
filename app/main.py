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
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)

    return len(students)


def read_groups_information() -> list[str]:
    specialty_names = set()

    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:
                group = pickle.load(groups_file)
                specialty_names.add(group.specialty.name)
            except EOFError:
                break

    return list(specialty_names)


def read_students_information() -> list[Student]:
    students = []

    with open("students.pickle", "rb") as students_file:
        while True:
            try:
                student = pickle.load(students_file)
                students.append(student)
            except EOFError:
                break

    return students
