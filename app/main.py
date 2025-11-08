from __future__ import annotations

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
    """Write all groups to 'groups.pickle' and return max student count."""
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = max((len(group.students) for group in groups), default=0)
    return max_students


def write_students_information(students: list[Student]) -> int:
    """Write all students to 'students.pickle' and return count."""
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list[str]:
    """Read 'groups.pickle' and return unique specialties' names."""
    with open("groups.pickle", "rb") as file:
        groups: list[Group] = pickle.load(file)

    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def read_students_information() -> list[Student]:
    """Read 'students.pickle' and return list of Student instances."""
    with open("students.pickle", "rb") as file:
        students: list[Student] = pickle.load(file)
    return students
