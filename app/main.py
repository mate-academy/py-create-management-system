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


def write_groups_information(lyceum_groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_in:
        pickle.dump(lyceum_groups, file_in)
    max_num = 0
    for group in lyceum_groups:
        if len(group.students) > max_num:
            max_num = len(group.students)
    return max_num


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_in:
        pickle.dump(students, file_in)
    return len(students)


def read_groups_information() -> set:
    specialties = []
    with open("groups.pickle", "rb") as file_in:
        lyceum_groups = pickle.load(file_in)
    for group in lyceum_groups:
        specialties.append(group.specialty.name)
    return set(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
