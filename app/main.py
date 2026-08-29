from datetime import date
import dataclasses
import pickle
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    top_group = 0
    for group in groups:
        if len(group.students) > top_group:
            top_group = len(group.students)
    return top_group


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_f:
        pickle.dump(students, pickle_f)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    result = []
    for group in groups:
        if group.specialty.name not in result:
            result.append(group.specialty.name)
    return result


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
