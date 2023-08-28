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
    with open("groups.pickle", "wb") as file_of_groups:
        pickle.dump(groups, file_of_groups)

    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_of_students:
        pickle.dump(students, file_of_students)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialty_names = set(group.specialty.name for group in groups)
    return specialty_names


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
