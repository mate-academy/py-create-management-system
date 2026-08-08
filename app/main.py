import dataclasses
import pickle
from datetime import date
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


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)
    max_count_students = 0
    for group in group_list:
        if max_count_students < len(group.students):
            max_count_students = len(group.students)
    return max_count_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialty = []
    for group in groups:
        specialty.append(group.specialty.name)
    return set(specialty)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    students_list = []
    for student in students:
        students_list.append(student)
    return students_list
