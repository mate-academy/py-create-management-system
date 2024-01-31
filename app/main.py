from datetime import datetime

import dataclasses
import pickle


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
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> list | int:

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if not groups:
        return []
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        specialties = set(group.specialty.name for group in groups)
    return list(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        student = pickle.load(pickle_file)
        students.extend(student)

    return students
