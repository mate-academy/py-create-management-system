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
    with open("groups.pickle", "wb") as handle:
        pickle.dump(groups, handle)
    if not groups:
        return 0
    return len(max(groups, key=lambda group: len(group.students)).students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as handle:
        pickle.dump(students, handle)
    return len(students)


def read_groups_information() -> list:
    groups = []
    with open("groups.pickle", "rb") as handle:
        groups.extend(pickle.load(handle))
    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    result = []
    with open("students.pickle", "rb") as handle:
        result.extend(pickle.load(handle))
    return result
