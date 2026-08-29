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
    address: list[str]


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Specialty]


def write_groups_information(list_groups: list[Group]) -> int:
    students = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_groups, file)
    for group in list_groups:
        students = max(students, len(group.students))
    return students


def write_students_information(list_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_students, file)
    return len(list_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        specialties = {group.specialty.name for group in groups}
        return specialties


def read_students_information() -> str:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
