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


def write_groups_information(groups: list[Group]) -> int:
    group_size = 0
    for group in groups:
        if len(group.students) > group_size:
            group_size = len(group.students)

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return group_size


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set:
    specialties_list = []
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    for group in groups:
        specialties_list.append(group.specialty.name)

    return set(specialties_list)


def read_students_information() -> list:
    all_students_list = []
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    for student in students:
        all_students_list.append(student)

    return all_students_list
