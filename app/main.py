from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: str


@dataclass
class Student:
    first_name : str
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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)
    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    number_students = len(students)
    return number_students


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
    specialy_name = set()
    for group in groups:
        specialy_name.add(group.specialty.name)
    return specialy_name


def read_students_information() -> None:
    with open("students.pickle", "rb") as students_file:
        student = pickle.load(students_file)
        return student
