import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


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
    course: str
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as gp:
        pickle.dump(groups, gp)
    if len(groups) != 0:
        return max([len(group.students) for group in groups])


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as sp:
        pickle.dump(students, sp)
    return len(students)


def read_groups_information() -> set:

    with open("groups.pickle", "rb") as gp:
        groups = pickle.load(gp)
        specialties = [group.specialty.name for group in groups]
    return set(specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as sf:
        students = pickle.load(sf)
    return students
