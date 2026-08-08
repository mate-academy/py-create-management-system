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
    students: list


def write_groups_information(groups: list) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


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
