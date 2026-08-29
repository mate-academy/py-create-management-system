from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
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
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set:
    path = Path("groups.pickle")
    if not path.exists() or path.stat().st_size == 0:
        return set()
    with path.open("rb") as f:
        groups: list[Group] = pickle.load(f)
    return {g.specialty.name for g in groups}


def read_students_information() -> list[Student]:
    path = Path("students.pickle")
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open("rb") as f:
        return pickle.load(f)
