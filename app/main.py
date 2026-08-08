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


def write_groups_information(group_info: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(group_info, groups_file)
    return max((len(group.students) for group in group_info), default=0)


def write_students_information(student_info: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(student_info, students_file)
    return len(student_info)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
        specialties = list({group.specialty.name for group in groups})
        return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as student_file:
        return pickle.load(student_file)
