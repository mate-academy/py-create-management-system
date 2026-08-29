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
    course: int | datetime
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    return sorted({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
