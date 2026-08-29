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


def write_groups_information(list_of_groups: list[Group]) -> int:
    max_students = 0 if len(list_of_groups) > 0 else None
    with open("groups.pickle", "wb") as pickle_file:
        for group in list_of_groups:
            pickle.dump(group, pickle_file)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in list_of_students:
            pickle.dump(student, pickle_file)
    return len(list_of_students)


def read_groups_information() -> list[str]:
    list_of_specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                if group.specialty.name not in list_of_specialties:
                    list_of_specialties.append(group.specialty.name)
            except EOFError:
                break
    return list_of_specialties


def read_students_information() -> list[Student]:
    list_of_students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                list_of_students.append(student)
            except EOFError:
                break
    return list_of_students
