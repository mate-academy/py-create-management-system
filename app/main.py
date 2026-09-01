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


def read_pickle(path: str) -> list:
    with open(path, "rb") as file:
        return pickle.load(file)


def write_pickle(path: str, items: list) -> None:
    with open(path, "wb") as file:
        pickle.dump(items, file)


def write_groups_information(groups: list[Group]) -> int:
    write_pickle("groups.pickle", groups)
    if not groups:
        return 0
    return len(sorted(groups, key=lambda group: len(groups))[0].students)


def write_students_information(students: list[Student]) -> int:
    write_pickle("students.pickle", students)
    return len(students)


def read_groups_information() -> list:
    groups = read_pickle("groups.pickle")
    return list({group.specialty.name for group in groups})


def read_students_information() -> list:
    students = read_pickle("students.pickle")
    return students
