import dataclasses
import pickle

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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)
    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
    groups_list = []
    for group in groups:
        if group.specialty.name not in groups_list:
            groups_list.append(group.specialty.name)
    return groups_list


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        students_list = pickle.load(students_file)
    return students_list
