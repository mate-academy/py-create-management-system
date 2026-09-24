import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> set:
    specialty_names = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
            except EOFError:
                break
            specialty_names.add(group.specialty.name)

    return specialty_names


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
            except EOFError:
                break
            students.append(student)

    return students
