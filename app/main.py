import dataclasses
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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: List[Specialty]
    course: int
    students: List[Student]


def write_groups_information(group):
    with open("groups.pickle", "wb") as f:
        pickle.dump(group, f)
    maximum = 0
    for i in group:
        if len(i.students) > maximum:
            maximum = len(i.students)
    return maximum


def write_students_information(student):
    with open("students.pickle", "wb") as f:
        pickle.dump(student, f)
    return len(student)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialty = []
    for group in groups:
        specialty.append(group.specialty.name)
    return set(specialty)


def read_students_information():
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
