import pickle
from datetime import datetime
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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0  # or raise an exception if appropriate

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    num_students = len(students)
    return num_students


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specialties = set(group.specialty.name for group in groups)
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
