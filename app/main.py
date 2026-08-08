from typing import List

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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups_list = pickle.load(f)

    return set([group.specialty.name for group in groups_list])


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)

    return students_list
