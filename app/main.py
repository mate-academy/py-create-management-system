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
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    return max((len(g.students) for g in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as file_py:
        groups = pickle.load(file_py)
    return set(group.specialty.name for group in groups)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_py:
        students = pickle.load(file_py)
    return [student for student in students]
