from dataclasses import dataclass
import pickle
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
    phone_number: int
    address: list[str]


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Specialty]


def write_groups_information(ls: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(ls, file)

    for group in ls:
        max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(ls: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(ls, file)
    return len(ls)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        specialties = {group.specialty.name for group in groups}
        return specialties


def read_students_information() -> str:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
