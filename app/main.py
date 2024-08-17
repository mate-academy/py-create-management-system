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
    birth_date: datetime.time
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_students_information(students: list[Student]) -> int:
    num_of_stud = 0
    with open("students.pickle", "wb") as pickle_file:
        for stud in students:
            pickle.dump(stud, pickle_file)
    num_of_stud = len(students)
    return num_of_stud


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for grp in groups:
            pickle.dump(grp, pickle_file)
        num_of_grp_of_std = 0
        for group in groups:
            if group.students is not None:
                if len(group.students) > num_of_grp_of_std:
                    num_of_grp_of_std = len(group.students)

    return num_of_grp_of_std


def read_groups_information() -> list:
    groups_speciality = []
    with open("groups.pickle", "rb") as pickle_file:
        try:
            while True:
                spec = pickle.load(pickle_file).specialty.name
                if spec not in groups_speciality:
                    groups_speciality.append(spec)
        except EOFError:
            pass

    return groups_speciality


def read_students_information() -> int:
    all_students = []
    with open("students.pickle", "rb") as pickle_file:
        try:
            while True:
                all_students.append(pickle.load(pickle_file))
        except EOFError:
            pass

    return all_students
