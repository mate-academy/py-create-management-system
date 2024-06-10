import pickle
from dataclasses import dataclass
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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    return len(max(groups, key=lambda group: len(group.students)).students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    groups = []
    with open("groups.pickle", "rb") as file:
        groups.extend(pickle.load(file))
    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list[Student]:
    result = []
    with open("students.pickle", "rb") as file:
        result.extend(pickle.load(file))
    return result
