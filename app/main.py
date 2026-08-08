import dataclasses
import pickle

from datetime import datetime
from os import path
from typing import List


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
    res = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            if len(group.students) > res:
                res = len(group.students)
    return res


def write_students_information(students: List[Student]) -> int:
    res = 0
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
            res += 1
    return res


def read_groups_information() -> list:
    if path.isfile("groups.pickle"):
        with open("groups.pickle", "rb") as file:
            res = set()
            while True:
                try:
                    res.add(pickle.load(file).specialty.name)
                except EOFError:
                    break
            return list(res)


def read_students_information() -> List[Student]:
    if path.isfile("students.pickle"):
        with open("students.pickle", "rb") as file:
            res = []
            while True:
                try:
                    res.append(pickle.load(file))
                except EOFError:
                    return res
