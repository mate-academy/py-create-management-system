from __future__ import annotations
import dataclasses
from typing import List
from datetime import date
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_list, f)
    try:
        return max(len(data.students) for data in groups_list)
    except ValueError:
        return 0


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    try:
        return len(students_list)
    except ValueError:
        return 0


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        data = pickle.load(f)
    res: dict = dict.fromkeys([i.specialty.name for i in data])
    return list(res.keys())


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
