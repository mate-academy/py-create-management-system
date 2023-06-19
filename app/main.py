import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = (max(len(group.students) for group in groups)
                    if groups else 0)
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max_students


def write_students_information(students: list[Student]) -> int:
    num_students = len(students)
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return num_students


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = {group.specialty.name for group in groups}
    return specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
