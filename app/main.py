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
    average_mark: [int, float]
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: Student


def write_groups_information(groups: list) -> int:
    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max_students


def write_students_information(students: str) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    speciality = set(group.specialty.name for group in groups)
    return list(speciality)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
