import dataclasses
from datetime import date
import pickle


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
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

    specialties = []

    for group in groups:
        if group.specialty.name not in specialties:
            specialties.append(group.specialty.name)

    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        return pickle.load(pickle_file)
