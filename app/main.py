from __future__ import annotations
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            pickle.dump(group, pickle_file)
    if not group_list:
        return 0
    return max(len(group.students) for group in group_list)


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_list:
            pickle.dump(student, pickle_file)
    return len(student_list)


def read_groups_information(pick_file: str = "groups.pickle") -> list:
    groups = []
    with open(pick_file, "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
            except EOFError:
                break
            groups.append(group)
    res = {group.specialty.name for group in groups}
    return list(res)


def read_students_information(pick_file: str = "students.pickle") -> list:
    studs = []
    with open(pick_file, "rb") as pickle_file:
        while True:
            try:
                stud = pickle.load(pickle_file)
            except EOFError:
                break
            studs.append(stud)
    return studs
