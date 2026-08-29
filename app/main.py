from datetime import datetime
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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    number_of_students = len(students)
    return number_of_students


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        group = pickle.load(pickle_file)
    group_set = set()
    for spec in group:
        group_set.add(spec.specialty.name)
    specialties_list = list(group_set)
    return specialties_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_f:
        students = pickle.load(pickle_f)
    return students
