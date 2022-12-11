import pickle

from typing import List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    max_students = 0
    for group in group_list:
        if len(group.students) > max_students:
            max_students = len(group.students)
    with open("groups.pickle", "wb") as pickle_group:
        pickle.dump(group_list, pickle_group)
    return max_students


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students_list, pickle_students)
    return len(students_list)


def read_groups_information() -> list:
    specialties_name = []
    with open("groups.pickle", "rb") as pickle_group:
        groups = pickle.load(pickle_group)
        for i in range(len(groups)):
            if groups[i].specialty.name not in specialties_name:
                specialties_name.append(groups[i].specialty.name)
    return specialties_name


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as pickle_students:
        students = pickle.load(pickle_students)
    return students
