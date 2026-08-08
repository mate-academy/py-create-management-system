import dataclasses
from datetime import datetime
import pickle


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


def write_groups_information(groups: list) -> int:
    max_number_students = 0
    if groups:
        max_number_students = max(len(group.students) for group in groups)
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)
    return max_number_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
    unique_specialities = set(group.specialty.name for group in groups)
    return list(unique_specialities)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return students
