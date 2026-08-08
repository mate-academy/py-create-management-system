import pickle

from dataclasses import dataclass
from datetime import datetime
from typing import List, Union


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


def write_groups_information(groups: List[Group]) -> Union[float, int]:
    student_list = []
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
            student_list.append(len(group.students))
        return max(student_list, default=0)


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students_list:
            pickle.dump(student, pickle_file)
        return len(students_list)


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as read_pickle:
        while True:
            try:
                specialties.add(pickle.load(read_pickle).specialty.name)
            except EOFError:
                break
        return list(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as read_pickle:
        while True:
            try:
                students.append(pickle.load(read_pickle))
            except EOFError:
                break
        return students
