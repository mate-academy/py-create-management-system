from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
import pickle
from os import PathLike


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
    has_scholarship: float
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(input_data: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(input_data, f)
    if input_data:
        return max(len(element.students) for element in input_data)


def write_students_information(input_data: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(input_data, f)
    return len([element for element in input_data
                if isinstance(element, Student)])


def read_groups_information(input_data: str | PathLike
                            = "groups.pickle") -> set:
    with open(input_data, "rb") as f:
        content = pickle.load(f)
    return set({element.specialty.name for element in content})


def read_students_information(input_data: str | PathLike
                              = "students.pickle") -> list:
    with open(input_data, "rb") as f:
        content = pickle.load(f)
    return content
