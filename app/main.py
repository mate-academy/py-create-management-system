import dataclasses
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: list):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    max_num = 0
    for group in groups:
        if len(group.students) > max_num:
            max_num = len(group.students)
    return max_num


def write_students_information(students_list: list):
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialties = []
    for group in groups:
        specialties.append(group.specialty.name)
    return set(specialties)


def read_students_information():
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)
    return students_list
