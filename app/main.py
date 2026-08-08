from __future__ import annotations

import pickle

import dataclasses

from typing import List

from datetime import datetime


@dataclasses.dataclass
class Specialty():
    name: str
    number: int


@dataclasses.dataclass
class Student():
    first_name: str
    last_name: int
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group():
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(group_list, group_file)
    if not group_list:
        return 0
    return max(len(group.students) for group in group_list)


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)
    return len(students_list)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
    return list(set(group.specialty.name for group in groups))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return students
