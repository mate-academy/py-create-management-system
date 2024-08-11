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
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(studs: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(studs, pickle_file)
    return len(studs)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    specialty_names = {group.specialty.name for group in groups}
    return specialty_names


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        studs = pickle.load(pickle_file)
    return studs
