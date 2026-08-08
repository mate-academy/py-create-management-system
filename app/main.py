from __future__ import annotations
import dataclasses
from datetime import datetime
import pickle


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
    specialty: Specialty   #
    course: int   # str date year
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_data_base:
        pickle.dump(list_of_groups, groups_data_base)
    if len(list_of_groups) > 0:
        return max([len(group.students) for group in list_of_groups])
    return 0


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_data_base:
        pickle.dump(list_of_students, students_data_base)
    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_data_base:
        list_of_groups = pickle.load(groups_data_base)
    return set([group.specialty.name for group in list_of_groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_data_base:
        list_of_students = pickle.load(students_data_base)
    return list_of_students
