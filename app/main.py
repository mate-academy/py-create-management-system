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


def write_groups_information(list_group: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_group, file)
    if not list_group:
        return 0
    return max(len(group.students) for group in list_group)


def write_students_information(list_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_students, file)
    return len(list_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        list_students = pickle.load(file)
    return list_students
