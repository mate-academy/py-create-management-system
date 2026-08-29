import pickle

from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0

    for group in groups:
        if len(group.students) >= max_students:
            max_students = len(group.students)

    with open("groups.pickle", "wb") as gr_pickle_file:
        pickle.dump(groups, gr_pickle_file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as st_pickle_file:
        pickle.dump(students, st_pickle_file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as gr_pickle_file:
        groups = pickle.load(gr_pickle_file)
    specialties = set([group.specialty.name for group in groups])

    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as st_pickle_file:
        students = pickle.load(st_pickle_file)

    return students
