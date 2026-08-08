from dataclasses import dataclass

import datetime

from typing import List

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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups, pickle_groups)
    return max(len(group.students)
               for group in groups) if groups else 0


def write_students_information(student: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(student, pickle_students)
        return len(student)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_groups:
        groups_list = pickle.load(pickle_groups)

    return set(group.specialty.name for group in groups_list)


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_student:
        student_list = pickle.load(pickle_student)
    return student_list
