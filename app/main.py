import pickle
from dataclasses import dataclass
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
    specialty: Specialty
    course: datetime.year
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    max_count_of_students = 0
    for group in groups:
        if len(group.students) > max_count_of_students:
            max_count_of_students = len(group.students)
    return max_count_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_file:
        group_specialties = set()
        for group in pickle.load(groups_file):
            group_specialties.add(group.specialty.name)
    return group_specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_file:
        students: list = []
        for student in pickle.load(students_file):
            students.append(student)
    return students
