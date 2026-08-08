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
    with open("groups.pickle", "wb") as gru_file:
        pickle.dump(groups, gru_file)
        return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as st_file:
        pickle.dump(students, st_file)
        return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as gru_file:
        groups = pickle.load(gru_file)
        return set(group.specialty.name for group in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as st_file:
        students = pickle.load(st_file)
        return students
