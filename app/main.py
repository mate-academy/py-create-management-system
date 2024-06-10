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


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max(len(groups.students) for group in groups)


def write_students_information(students: list) -> int:
    with open("students_pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specs = {group.speciality.name for group in groups}
    return list(specs)


def read_students_information() -> list:
    with open("students_pickle", "rb") as f:
        students = pickle.load(f)

    return students
