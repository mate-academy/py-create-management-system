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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)

    max_students = 0
    for group in group_list:
        if max_students < len(group.students):
            max_students = len(group.students)

    return max_students


def write_students_information(student_list: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(student_list, pickle_file)

    return len(student_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups_list = pickle.load(pickle_file)

    group_spec = {}

    for group in groups_list:
        group_spec[group.specialty.name] = 0
    result = []

    for key in group_spec.keys():
        result.append(key)

    return result


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students_list = pickle.load(pickle_file)

    return students_list
