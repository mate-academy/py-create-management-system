from datetime import datetime
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
    birth_date: datetime
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
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> set:
    items = []
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    items.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return set()

    return {group.specialty.name for group in items}


def read_students_information() -> list:
    items = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    items.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return items
