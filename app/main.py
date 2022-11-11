import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


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


def write_groups_information(groups: List[Group]) -> int:
    max_number_group_of_student = 0
    with open("groups.pickle", "wb") as groups_pickle_file:
        pickle.dump(groups, groups_pickle_file)
    for group in groups:
        if max_number_group_of_student < len(group.students):
            max_number_group_of_student = len(group.students)
    return max_number_group_of_student


def write_students_information(students: List[Student]) -> int:
    number_of_students = len(students)
    with open("students.pickle", "wb") as students_pickle_file:
        pickle.dump(students, students_pickle_file)
    return number_of_students


def read_groups_information() -> list:
    groups_specialty = []
    with open("groups.pickle", "rb") as groups_pickle_file:
        groups = pickle.load(groups_pickle_file)
    for group in groups:
        groups_specialty.append(group.specialty.name)
    return list(set(groups_specialty))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_pickle_file:
        students = pickle.load(students_pickle_file)
    return students
