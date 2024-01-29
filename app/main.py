import dataclasses
from datetime import datetime
import pickle
from typing import List


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        return 0

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> set:
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
            specialties_names = set(group.specialty.name for group in groups)
    except FileNotFoundError:
        specialties_names = set()

    return specialties_names


def read_students_information() -> None:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
