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


def write_groups_information(groups_information: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_information, f)

    if not groups_information:
        return 0

    max_students = max(len(group.students) for group in groups_information)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as s:
        pickle.dump(students, s)

    quantity_of_students = len(students)
    return quantity_of_students


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialties = set(group.specialty.name for group in groups)
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
