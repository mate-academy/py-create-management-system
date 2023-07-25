from typing import List

import dataclasses
import pickle

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
    max_group_size = 0

    for group in groups:
        if len(group.students) > max_group_size:
            max_group_size = len(group.students)

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max_group_size


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> set:
    specialties_list = []

    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    for group in groups:
        specialties_list.append(group.specialty.name)

    return set(specialties_list)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)

    return students_list
