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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)
    students_count = 0
    for group in group_list:
        if students_count < len(group.students):
            students_count = len(group.students)

    return students_count


def write_students_information(students_list: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = []
    for group in groups:
        specialties.append(group.specialty.name)
    return set(specialties)


def read_students_information() -> Student:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
