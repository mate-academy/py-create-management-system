import pickle
import dataclasses
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(
        group_instances: list[Group]
) -> int:
    with open("groups.pickle", "wb") as file:
        for group in group_instances:
            pickle.dump(group, file)
    maximum = 0
    for group in group_instances:
        if len(group.students) > maximum:
            maximum = len(group.students)
    return maximum


def write_students_information(
        student_instances: list[Student]
) -> int:
    with open("students.pickle", "wb") as file:
        for student in student_instances:
            pickle.dump(student, file)
    return len(student_instances)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break
    return students
