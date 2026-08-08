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
    specialty: List[str]
    course: int
    students: List[str]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file_g:
        pickle.dump(groups, file_g)
        current_max_number = 0
        for group in groups:
            pickle.dump(group, file_g)
            if len(group.students) > current_max_number:
                current_max_number = len(group.students)
    return current_max_number


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file_s:
        pickle.dump(students, file_s)
        amount = 0
        for student in students:
            pickle.dump(student, file_s)
            amount += 1
    return amount


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_gr:
        groups = pickle.load(file_gr)
        name_specialty = []
        for group in groups:
            name_specialty.append(group.specialty.name)
    return set(name_specialty)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_st:
        list_students = pickle.load(file_st)
    return list_students
