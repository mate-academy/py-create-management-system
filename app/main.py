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
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[str]:
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
            specialties = {group.specialty.name for group in groups}
            return list(specialties)
    except (FileNotFoundError, EOFError):
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []
