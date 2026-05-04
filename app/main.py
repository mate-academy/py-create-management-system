import dataclasses
import pickle
from datetime import date


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    students_count = 0
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    for group in groups:
        if students_count < len(group.students):
            students_count = len(group.students)

    return students_count


def write_students_information(students: list[Student]) -> int :
    students_count = 0
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    for student in students:
        students_count += 1

    return students_count


def read_groups_information() -> set:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as pickle_file:
            groups = pickle.load(pickle_file)
    except FileNotFoundError:
        return specialties

    for group in groups:
        specialties.add(group.specialty.name)

    return specialties


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as pickle_file:
            students = pickle.load(pickle_file)
    except FileNotFoundError:
        return []

    return students
