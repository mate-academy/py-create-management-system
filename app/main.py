from __future__ import annotations
from dataclasses import dataclass
from typing import List
from datetime import datetime
import pickle


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> None:
    result = []
    file_name = "groups.pickle"
    with open(file_name, "wb") as file_obj:
        pickle.dump(groups, file_obj)

    for group in groups:
        for student in group.students:
            if student not in result:
                result.append(student)

    return len(result)


def write_students_information(students: List[Student]) -> None:
    file_name = "students.pickle"
    with open(file_name, "wb") as file_obj:
        pickle.dump(students, file_obj)

    return len(students)


def read_groups_information() -> None:
    result = []
    groups = []
    file_name = "groups.pickle"
    with open(file_name, "rb") as file_obj:
        groups = pickle.load(file_obj)

    if groups:
        for group in groups:
            if group.specialty.name not in result:
                result.append(group.specialty.name)

    return result


def read_students_information() -> None:
    students = []
    file_name = "students.pickle"
    with open(file_name, "rb") as file_obj:
        students = pickle.load(file_obj)

    return students
