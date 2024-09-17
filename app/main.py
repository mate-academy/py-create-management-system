from datetime import datetime
from dataclasses import dataclass
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_of_students = 0

    for group in groups:
        if max_of_students < len(group.students):
            max_of_students = len(group.students)

    return max_of_students


def write_students_information(students: List[Student]):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specialities = set()

    for group in groups:
        specialities.add(group.specialty.name)

    return list(specialities)


def read_students_information():
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
