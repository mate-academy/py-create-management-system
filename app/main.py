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


def write_groups_information(inputs: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(inputs, file)

    if inputs:
        return max(len(group.students) for group in inputs)


def write_students_information(inputs: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(inputs, file)

    return len(inputs)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
