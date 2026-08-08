from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
import pickle


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
    course: int
    students: list[Student]


def write_groups_information(lyceum_group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(lyceum_group_list, pickle_file)

    max_students = []
    if lyceum_group_list != []:
        max_students = max(len(group.students) for group in lyceum_group_list)

    return max_students


def write_students_information(group_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)

    return len(group_list)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

    speciality_uniq = list(set(group.specialty.name for group in groups))
    return speciality_uniq


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
