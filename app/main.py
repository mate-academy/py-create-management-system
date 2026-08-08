from dataclasses import dataclass
from datetime import datetime

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
    average_mark: int
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickled_file:
        pickle.dump(groups, pickled_file)
    students = [len(group.students) for group in groups]
    if students:
        max_students = max(students)
        return max_students
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickled_file:
        pickle.dump(students, pickled_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickled_file:
        groups = pickle.load(pickled_file)
    return {group.specialty.name for group in groups}


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickled_file:
        students = pickle.load(pickled_file)
    return students
