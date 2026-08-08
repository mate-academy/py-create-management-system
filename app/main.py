from dataclasses import dataclass

import pickle

import datetime

from typing import List


@dataclass
class Specialty:
    name: str
    number: str


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as gr_file:
        pickle.dump(groups, gr_file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as st_file:
        pickle.dump(students, st_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as gr_file:
        groups = pickle.load(gr_file)
    return set({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as st_file:
        students = pickle.load(st_file)
    return students
