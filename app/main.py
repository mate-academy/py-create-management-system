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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> None:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            max_students = max(max_students, len(group.students))

    return max_students


def write_students_information(students: List[Student]) -> None:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> list:
    specialization = set()
    with open("groups.pickle", "rb") as f:
        try:
            while True:
                group = pickle.load(f)
                specialization.add(group.specialty.name)

        except EOFError:
            pass

    return list(specialization)


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as f:
        try:
            while True:
                students_list.append(pickle.load(f))

        except EOFError:
            pass

    return students_list
