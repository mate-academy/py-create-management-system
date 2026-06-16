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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    total_students = max(len(group.students) for group in groups)

    return total_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information(file_name: str = "groups.pickle") -> set:
    with open(file_name, "rb") as f:
        groups = pickle.load(f)

    return set(group.specialty.name for group in groups)


def read_students_information(file_name: str = "students.pickle") -> list:
    with open(file_name, "rb") as f:
        students = pickle.load(f)

    return students
