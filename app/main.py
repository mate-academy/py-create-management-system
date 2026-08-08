from __future__ import annotations
import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
            if max_students < len(group.students):
                max_students = len(group.students)
    return max_students


def write_students_information(students: list) -> int:
    students_number = 0
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
            students_number += 1
    return students_number


def read_groups_information() -> set:
    spec = set()
    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:
                group = pickle.load(groups_file)
                spec.add(group.specialty.name)
            except EOFError:
                return spec


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as students_file:
        while True:
            try:
                student = pickle.load(students_file)
                students.append(student)
            except EOFError:
                return students
