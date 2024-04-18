import datetime
import pickle
from dataclasses import dataclass


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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as group_file:
        for group in groups:
            max_students = max(max_students, len(group.students))
        pickle.dump(groups, group_file)
    return max_students


def write_students_information(students: list[Student]) -> int:
    number_of_students = len(students)
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)
    return number_of_students


def read_groups_information() -> list:
    specialties_names = []
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
        for group in groups:
            if group.specialty.name not in specialties_names:
                specialties_names.append(group.specialty.name)
    return specialties_names


def read_students_information() -> list:
    with open("students.pickle", "rb") as student_file:
        student_list = pickle.load(student_file)
    return student_list
