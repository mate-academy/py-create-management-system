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


def write_groups_information(groups):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    num_students = len(students)
    return num_students


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialty = set(group.specialty.name for group in groups)
    return list(specialty)


def read_students_information():
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
