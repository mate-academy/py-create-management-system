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


def write_groups_information(groups: list[Group]) -> int:
    students = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            students.append(len(group.students))

    return max(students, default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> set[str]:
    specialty_names = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
            except EOFError:
                break

            specialty_names.add(group.specialty.name)
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
