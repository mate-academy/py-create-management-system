from dataclasses import dataclass
from datetime import datetime
from typing import List
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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_of_group: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_pickle:
        pickle.dump(list_of_group, groups_pickle)
    n_students = 0
    for group in list_of_group:
        if len(group.students) > n_students:
            n_students = len(group.students)
    return n_students


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(list_of_students, students_pickle)
    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_out:
        groups = pickle.load(groups_out)
    groups_specialities = []
    for group in groups:
        groups_specialities.append(group.specialty.name)
    return set(groups_specialities)


def read_students_information() -> str:
    with open("students.pickle", "rb") as students_out:
        students = pickle.load(students_out)
    return students
