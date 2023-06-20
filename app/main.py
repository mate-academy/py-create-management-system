from dataclasses import dataclass
from datetime import date
from functools import reduce
import pickle

from app.settings import settings


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    __write_data(groups, "groups_file")
    return reduce(lambda res, group: max(res, len(group.students)), groups, 0)


def write_students_information(students: list[Student]) -> int:
    __write_data(students, "students_file")
    return len(students)


def __write_data(data: list, file_key: str) -> None:
    with open(settings[file_key], "wb") as writer:
        pickle.dump(data, writer)


def __read_data(file_key: str) -> list:
    with open(settings[file_key], "rb") as reader:
        return pickle.load(reader)


def read_groups_information() -> list[str]:
    return list(
        set(
            group.specialty.name
            for group in __read_data("groups_file")
        )
    )


def read_students_information() -> list[Student]:
    return __read_data("students_file")
