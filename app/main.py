from __future__ import annotations

import pickle
import dataclasses
from datetime import datetime
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


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file_group_of_students:
        count_of_students = 0
        for group in groups:
            pickle.dump(group, file_group_of_students)
            if len(group.students) > count_of_students:
                count_of_students = len(group.students)
        return count_of_students


def write_students_information(list_of_students: list) -> int:
    with open("students.pickle", "wb") as file_of_students:
        number_of_students = 0
        for student in list_of_students:
            pickle.dump(student, file_of_students)
            number_of_students += 1
        return number_of_students


def read_groups_information() -> list:
    result = []
    students_group = []
    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:
                students_group.append(pickle.load(groups_file))
            except EOFError:
                break
        for length_group in range(len(students_group)):
            if students_group[length_group].specialty.name not in result:
                result.append(students_group[length_group].specialty.name)
        return result


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as students_file:
        while True:
            try:
                students.append(pickle.load(students_file))
            except EOFError:
                break
        return students
