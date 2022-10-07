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

    return max([len(info.students) for info in groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups_info = pickle.load(file)

    return list({info.specialty.name for info in groups_info})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students_info = pickle.load(file)

    return students_info
