import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
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

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_number = max((len(group.students) for group in groups), default=0)

    return max_number


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    unique_groups = set()

    for group in groups:
        unique_groups.add(group.specialty.name)

    return list(unique_groups)


def read_students_information() -> list:

    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
