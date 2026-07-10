from typing import List
import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: str


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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specialties = set()
    for group in groups:
        specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
