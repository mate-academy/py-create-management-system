import dataclasses
from datetime import date
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_groups):
    for group in list_groups:
        with open("groups.pickle", "wb") as f:
            pickle.dump(group, f)
    maximum_students = max([len(num.students) for num in list_groups])
    return maximum_students


def write_students_information(list_student):
    for student in list_student:
        with open("students.pickle", "wb") as f:
            pickle.dump(student, f)
    number_students = len(list_student)
    return number_students


def read_groups_information():
    groups = []
    while True:
        try:
            with open("groups.pickle", "rb") as f:
                group = pickle.load(f)
            groups.append(group.specialty.name)
        except EOFError:
            break
    return set(groups)


def read_students_information():
    students = []
    while True:
        try:
            with open("students.pickle", "rb") as f:
                group = pickle.load(f)
            students.append(group)
        except EOFError:
            break
    return students
