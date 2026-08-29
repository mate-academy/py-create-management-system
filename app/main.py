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


def write_groups_information(groups: str) -> None:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: str) -> None:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> None:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specialties = []
    for group in groups:
        if group.specialty.name not in specialties:
            specialties.append(group.specialty.name)
    return specialties


def read_students_information() -> None:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
