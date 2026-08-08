import os
import pickle
from dataclasses import dataclass
from datetime import datetime


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    return max([len(group.students) for group in groups])


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        if os.path.getsize("groups.pickle") > 0:
            specialties = set(
                group.specialty.name for group in pickle.load(f)
            )
    return list(specialties)


def read_students_information() -> int:
    with open("students.pickle", "rb") as f:
        if os.path.getsize("students.pickle") > 0:
            return pickle.load(f)
