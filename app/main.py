import dataclasses
import pickle

from datetime import datetime
#from __future__ import annotations


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime  # TODO: Clarify that!
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int  # TODO: Clarify that!
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    num_of_students_in_groups = []
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            num_of_students_in_groups.append(len(group.students))
            pickle.dump(group, pickle_file)
    return max(num_of_students_in_groups)


def write_students_information(students: list[Student]) -> int:
    num_of_students = 0
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            num_of_students += 1
            pickle.dump(student, pickle_file)
    return num_of_students


def read_groups_information() -> list[str]:
    specialties_names = {}
    with open("groups.pickle", "rb") as pickle_file:
        specialty = pickle.load(pickle_file)
        # specialties_names
