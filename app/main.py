import dataclasses
from datetime import date
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str = None
    number: int = None


@dataclasses.dataclass
class Student:
    first_name: str = None
    last_name: str = None
    birth_date: date = None
    average_mark: float = None
    has_scholarship: bool = None
    phone_number: str = None
    address: str = None


@dataclasses.dataclass
class Group:
    specialty: Specialty = None
    course: int = None
    students: List[Student] = None


def write_groups_information(list_groups):

    with open("groups.pickle", "wb") as f:
        for group in list_groups:
            pickle.dump(group, f)
    maximum_students = max([len(num.students) for num in list_groups])\
        if len(list_groups) else 0
    return maximum_students


def write_students_information(list_student):
    with open("students.pickle", "wb") as f:
        for student in list_student:
            pickle.dump(student, f)
    number_students = len(list_student)
    return number_students


def read_groups_information():
    groups = []
    with open("groups.pickle", "rb") as f:
        try:
            while True:
                group = pickle.load(f)
                groups.append(group.specialty.name)
        except EOFError:
            pass
    return set(groups)


def read_students_information():
    students = []
    with open("students.pickle", "rb") as f:
        try:
            while True:
                group = pickle.load(f)
                students.append(group)
        except EOFError:
            pass
    return students
