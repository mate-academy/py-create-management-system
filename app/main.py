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
    max_students = float("-inf")

    with open("groups.pickle", "wb") as file:
        for group in groups:
            max_students = max(max_students, len(group.students))
            pickle.dump(group, file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list[str]:
    specialties = set()

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
            except EOFError:
                break

    return list(specialties)


def read_students_information() -> list[Student]:
    students: list[Student] = []

    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break

    return students
