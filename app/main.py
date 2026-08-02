from dataclasses import dataclass
from typing import List
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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    all_students = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            all_students.append(len(group.students))
    return max(all_students, default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list:
    specialties = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                if group.specialty.name not in specialties:
                    specialties.append(group.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list:
    result_list = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                result_list.append(student)
            except EOFError:
                break
    return result_list
