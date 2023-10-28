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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_size_of_group = 0
    for group in groups:
        if len(group.students) > max_size_of_group:
            max_size_of_group = len(group.students)
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max_size_of_group


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    uniq_specializations = []
    for group in groups:
        if group.specialty.name not in uniq_specializations:
            uniq_specializations.append(group.specialty.name)
    return uniq_specializations


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
