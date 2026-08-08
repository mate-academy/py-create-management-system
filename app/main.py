import pickle
import dataclasses
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as groups_data_file:
        for group in groups:
            students_quantity = len(group.students)
            if students_quantity > max_students:
                max_students = students_quantity
            pickle.dump(group, groups_data_file)

    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_data_file:
        for student in students:
            pickle.dump(student, students_data_file)
    number_of_students = len(students)
    return number_of_students


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        specialities = []
        while True:
            try:
                group = pickle.load(pickle_file)
                if group.specialty.name not in specialities:
                    specialities.append(group.specialty.name)
            except EOFError:
                break
    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = []
        while True:
            try:
                student = pickle.load(pickle_file)
                if isinstance(student, Student):
                    students.append(student)
            except EOFError:
                break
    return students
