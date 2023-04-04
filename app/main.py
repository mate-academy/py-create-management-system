from dataclasses import dataclass

import pickle

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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: datetime.year
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)
        max_count = 0
        for group in groups:
            if len(group.students) > max_count:
                max_count = len(group.students)
    return max_count


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)
    return len(students)


def read_groups_information() -> list:
    specialties = list()
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
        for group in groups:
            if group.specialty.name not in specialties:
                specialties.append(group.specialty.name)

    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as student_file:
        students = list(pickle.load(student_file))
    return students
