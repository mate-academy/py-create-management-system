from __future__ import annotations

import dataclasses
import pickle
from typing import List
from datetime import datetime


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
    students: List[Student]


def write_groups_information(groups_information: List[Group]) -> int | None:
    with open("groups.pickle", "wb") as groups_information_file:
        pickle.dump(groups_information, groups_information_file)
    if not groups_information:
        return
    return max([len(group.students) for group in groups_information])


def write_students_information(students_information: List[Student]) -> int:
    with open("students.pickle", "wb") as students_information_file:
        pickle.dump(students_information, students_information_file)
    return len(students_information)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as groups_information_file:
        while True:
            try:
                group = pickle.load(groups_information_file)
            except EOFError:
                break
        specialties_names = []
        for group_ in group:
            if group_.specialty not in specialties_names:
                specialties_names.append(group_.specialty.name)
        return list(set(specialties_names))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_information_file:
        while True:
            try:
                student = pickle.load(students_information_file)
            except EOFError:
                break
        return student
