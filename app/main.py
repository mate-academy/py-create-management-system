import dataclasses
import pickle

from datetime import datetime
from typing import List


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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_student = 0
    with open("groups.pickle", "wb") as group_file:
        for group in groups:
            pickle.dump(group, group_file)
            max_student = max(max_student, len(group.students))
    return max_student


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in students:
            pickle.dump(student, student_file)
    return len(students)


def read_groups_information() -> set:
    specialties_name = set()
    with open("groups.pickle", "rb") as group_file:
        while True:
            try:
                group = pickle.load(group_file)
                specialties_name.add(group.specialty.name)
            except EOFError:
                break
    return specialties_name


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break
    return students
