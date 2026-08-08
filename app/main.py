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
    address: int


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_number_of_students_in_group = 0
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    for group in groups:
        if len(group.students) > max_number_of_students_in_group:
            max_number_of_students_in_group = len(group.students)
    return max_number_of_students_in_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list[str]:
    specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    for group in groups:
        if group.specialty.name not in specialties:
            specialties.append(group.specialty.name)
    return specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        return pickle.load(pickle_file)
