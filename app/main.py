import dataclasses

from datetime import datetime

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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as gr:
        pickle.dump(groups, gr)
    try:
        count = max([len(group.students) for group in groups])
    except ValueError:
        count = 0

    return count


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as st:
        pickle.dump(students, st)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as gr:
        groups = pickle.load(gr)
    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as st:
        students = pickle.load(st)
    return students
