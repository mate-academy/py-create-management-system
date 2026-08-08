import pickle

from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: List[Specialty]
    course: float
    students: List[Student]


def write_groups_information(groups):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students = 0
    for i in groups:
        if len(i.students) > max_students:
            max_students = len(i.students)
    return max_students


def write_students_information(students):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    all_specialties = []
    for group in groups:
        all_specialties.append(group.specialty.name)
    return set(all_specialties)


def read_students_information():
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
