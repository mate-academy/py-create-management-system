import pickle

from dataclasses import dataclass
from typing import List
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
    specialty: object
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    number_of_students = []
    with open("groups.pickle", "wb") as file_groups:
        for group in groups:
            pickle.dump(group, file_groups)
            number_of_students.append(len(group.students))
        if number_of_students:
            return max(number_of_students)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_groups:
        for student in students:
            pickle.dump(student, file_groups)
    return len(students)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as file_groups:
        try:
            while True:
                specialties.add((pickle.load(file_groups)).specialty.name)
        except EOFError:
            return specialties


def read_students_information() -> list:
    list_of_students = []
    with open("students.pickle", "rb") as file_students:
        try:
            while True:
                list_of_students.append(pickle.load(file_students))
        except EOFError:
            return list_of_students
