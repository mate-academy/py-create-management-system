from dataclasses import dataclass
from datetime import datetime
import pickle
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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
    return (
        max([len(group.students) for group in groups])
        if groups else 0
    )


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        try:
            groups_specialties = []
            while True:
                group = pickle.load(pickle_file)
                groups_specialties.append(group.specialty.name)
        except EOFError:
            return set(groups_specialties)


def read_students_information() -> List:
    with open("students.pickle", "rb") as pickle_file:
        try:
            students = []
            while True:
                student = pickle.load(pickle_file)
                students.append(student)
        except EOFError:
            return students
