from __future__ import annotations

import dataclasses
import pickle


from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    max_group = 0
    for group in group_list:
        length = len(group.students)
        if length > max_group:
            max_group = length
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    return max_group


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialty_list = []
    for group in groups:
        specialty_list.append(group.specialty.name)
    return set(specialty_list)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
