import pickle
from datetime import datetime
from dataclasses import dataclass
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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)

    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> set:
    groups = []
    with open("groups.pickle", "rb") as pickle_file:
        if len(pickle_file.read()) == 0:
            return []
        group = pickle.load(pickle_file)
        groups.append(group)

    specialties = set()
    for group in groups:
        specialties.add(group.specialty)
    return specialties


def read_students_information() -> List[Student]:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        student = pickle.load(pickle_file)
        students.append(student)
    return students
    # with open("students.pickle", "rb") as pickle_file:
    #     students = pickle.load(pickle_file)
    # return students
