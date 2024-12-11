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


def write_groups_information(list_group_inst: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_group_inst, f)
    max_students = 0
    for group in list_group_inst:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(list_students_inst: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_students_inst, f)
    return len(list_students_inst)


def read_groups_information() -> set:
    specialty_list = []
    with open("groups.pickle", "rb") as f:
        for group in pickle.load(f):
            specialty_list.append(group.specialty.name)
    return set(specialty_list)


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as f:
        for student in pickle.load(f):
            students_list.append(student)
    return students_list
