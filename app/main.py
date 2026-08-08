from dataclasses import dataclass
import pickle
from typing import List
from datetime import datetime


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_list, f)

    result = 0
    for group in groups_list:
        if len(group.students) > result:
            result = len(group.students)
    return result


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)

    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups_list = pickle.load(f)

    specialities_list = []
    for group in groups_list:
        if group.specialty.name not in specialities_list:
            specialities_list.append(group.specialty.name)
    return specialities_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)

    return students_list
