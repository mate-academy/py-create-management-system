from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int | float


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
    qty_of_students = 0
    for group in groups:
        if qty_of_students < len(group.students):
            qty_of_students = len(group.students)
    return qty_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set[list]:
    with open("groups.pickle", "rb") as file:
        data = pickle.load(file)
        return set([group.specialty.name for group in data])


def read_students_information() -> None:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
