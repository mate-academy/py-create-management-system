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
    max_number = 0
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    for group in groups:
        number = len(group.students)
        max_number = max(max_number, number)
    return max_number


def write_students_information(students: list[Student]) -> int:
    total_number = 0
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    for _ in students:
        total_number += 1
    return total_number


def read_groups_information() -> list:
    specialty_names = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        for group in groups:
            if group.specialty.name not in specialty_names:
                specialty_names.append(group.specialty.name)
    return specialty_names


def read_students_information() -> list:
    student_instances = []
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
        for student in students:
            student_instances.append(student)
    return student_instances
