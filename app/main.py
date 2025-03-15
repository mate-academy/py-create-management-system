from __future__ import annotations
from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_out:
        pickle.dump(groups, file_out)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> set:
    try:
        with open("groups.pickle", "rb") as pickle_file:
            groups = pickle.load(pickle_file)
        return {group.specialty.name for group in groups}
    except (FileNotFoundError, EOFError):
        return set()


def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as pickle_file:
            return pickle.load(pickle_file)
    except (FileNotFoundError, EOFError):
        return []
