import dataclasses
from datetime import datetime
import pickle


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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students) if students else 0


def read_groups_information() -> set[str]:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                try:
                    group = pickle.load(file)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No groups pickle file found.")
    return specialties


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                try:
                    student = pickle.load(file)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No students pickle file found.")
    return students
