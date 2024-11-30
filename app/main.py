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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_name:
        pickle.dump(groups, file_name)

    if groups:
        return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_name:
        pickle.dump(students, file_name)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_name:
        groups = pickle.load(file_name)

    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_name:
        students = pickle.load(file_name)
    return students
