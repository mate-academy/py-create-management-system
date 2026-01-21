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
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
    except EOFError:
        pass

    return list(specialties)


def read_students_information() -> list:
    students = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                student = pickle.load(file)
                students.append(student)
    except EOFError:
        pass

    return students
