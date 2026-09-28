from dataclasses import dataclass
import pickle
import os
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    if len(groups) == 0:
        return 0
    max_students = len(groups[0].students)
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
            max_students = max(max_students, len(groups[0].students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list:
    group_specialties = []

    if not os.path.exists("groups.pickle"):
        return []

    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
            except EOFError:
                break
            if group.specialty.name not in group_specialties:
                group_specialties.append(group.specialty.name)
    return group_specialties


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
            except EOFError:
                break
            students.append(student)
    return students
