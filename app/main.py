import dataclasses
import pickle

from typing import List
from datetime import datetime


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


open("groups.pickle", "wb")
open("student.pickle", "wb")


def write_groups_information(groups: List[Group]):
    l_students = []
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    for group in groups:
        l_students.append(len(group.students))
    if l_students:
        return max(l_students)
    return []


def write_students_information(studs: List[Student]):
    with open("students.pickle", "wb") as f:
        pickle.dump(studs, f)
        return len(studs)


def read_groups_information():
    l_speciality = []
    with open("groups.pickle", "rb") as f:
        data = pickle.load(f)
        for group in data:
            l_speciality.append(group.specialty.name)
        l_speciality = set(l_speciality)
        return l_speciality


def read_students_information():
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
