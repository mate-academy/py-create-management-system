from dataclasses import dataclass
import pickle
from datetime import datetime


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
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    student_lists = []
    if groups:
        for group in groups:
            student_lists.append(len(group.students))
        max_students = max(student_lists)
    else:
        max_students = 0
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set:
    specialty_set = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    for group in groups:
        specialty_set.append(group.specialty.name)
    return set(specialty_set)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
