import pickle
import dataclasses
from typing import List


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


def write_groups_information(groups: list):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    max_number = 0
    for pupils in groups:
        if len(pupils.students) > max_number:
            max_number = len(pupils.students)
    return max_number


def write_students_information(students: list):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialty_ = []
    for group in groups:
        specialty_.append(group.specialty.name)
    return set(specialty_)


def read_students_information():
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
