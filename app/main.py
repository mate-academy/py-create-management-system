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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as groups_information:
        pickle.dump(students, groups_information)

    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as groups_information:
        groups = pickle.load(groups_information)

    specialties = {group.specialty.name for group in groups}
    return specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as groups_information:
        student = pickle.load(groups_information)

    return student
