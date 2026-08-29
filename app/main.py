from __future__ import annotations
import dataclasses
import pickle
import datetime


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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(grups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as f:
        pickle.dump(grups, f)
        for group in grups:
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(stud: [Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(stud, f)
    return len(stud)


def read_groups_information() -> list:
    ls = []
    with open("groups.pickle", "rb") as f:
        info = pickle.load(f)
    for gr in info:
        if gr.specialty.name not in ls:
            ls.append(gr.specialty.name)
    return ls


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        inf_stud = pickle.load(f)
    return inf_stud
