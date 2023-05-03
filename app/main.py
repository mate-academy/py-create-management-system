from dataclasses import dataclass

from datetime import datetime

from typing import Union, List

import pickle


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
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: Union[int, datetime]
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students_group = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            if len(group.students) > max_students_group:
                max_students_group = len(group.students)
            pickle.dump(group, pickle_file)
    return max_students_group


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list:
    read_groups = []
    groups_specialties_names = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                read_groups.append(pickle.load(pickle_file))
            except EOFError:
                break
    for read_group in read_groups:
        groups_specialties_names.add(read_group.specialty.name)
    return list(groups_specialties_names)


def read_students_information() -> List[Student]:
    students_list = []
    with open("students.pickle", "rb") as students_file:
        while True:
            try:
                students_list.append(pickle.load(students_file))
            except EOFError:
                break
    return students_list
