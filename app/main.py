from dataclasses import dataclass
from datetime import datetime
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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pick_file:
        pickle.dump(groups, pick_file)
    if not groups:
        return 0
    return len(max(groups, key=lambda group: len(group.students)).students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pick_file:
        pickle.dump(students, pick_file)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pick_file:
        data: list[Group] = pickle.load(pick_file)
    return list(set(group.specialty.name for group in data))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pick_file:
        data: list[Student] = pickle.load(pick_file)
    return data
