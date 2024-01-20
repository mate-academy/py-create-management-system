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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        biggest_group = 0
        for group in groups:
            pickle.dump(group, pickle_file)
            if len(group.students) > biggest_group:
                biggest_group = len(group.students)
        return biggest_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
        return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        specialties = set()

        while True:
            try:
                group = pickle.load(pickle_file)
                specialties.add(group.specialty.name)
            except EOFError:
                break

        return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = []

        while True:
            try:
                students.append(pickle.load(pickle_file))
            except EOFError:
                break

        return students
