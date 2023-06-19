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
    course: datetime
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
            max_students = (len(group.students)
                            if len(group.students) > max_students
                            else max_students)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
    return len(students)


def read_groups_information() -> set:
    specialities = []
    with open("groups.pickle", "rb") as groups_file:
        try:
            while True:
                group = pickle.load(groups_file)
                specialities.append(group.specialty.name)
        except EOFError:
            pass
    return set(specialities)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as students_file:
        try:
            while True:
                student = pickle.load(students_file)
                students.append(student)
        except EOFError:
            pass
    return students
