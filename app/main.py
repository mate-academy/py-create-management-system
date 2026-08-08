from dataclasses import dataclass
from datetime import datetime
from typing import List
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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as group_file:
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)

            pickle.dump(group, group_file)
    return max_students


def write_students_information(students: List[Student]) -> int:
    num_students = len(students)
    with open("students.pickle", "wb") as stud_file:
        for student in students:
            pickle.dump(student, stud_file)
    return num_students


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as read_file:
        while True:
            try:
                group = pickle.load(read_file)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as read_file:
        while True:
            try:
                student = pickle.load(read_file)
                students.append(student)
            except EOFError:
                break
    return students
