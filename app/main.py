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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_students_information(students: list[Student]) -> None:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0
    biggest_group = max(groups, key=lambda group: len(group.students))
    return len(biggest_group.students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    unique_groups_specialty = set()
    for group in groups:
        unique_groups_specialty.add(group.specialty.name)
    return list(unique_groups_specialty)
