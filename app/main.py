import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if groups:
        max_students = max(
            len(group.students) for group in groups
        )
    else:
        max_students = 0
    return max_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
        for group in groups:
            specialties.add(group.specialty.name)
    except (FileNotFoundError, EOFError):
        pass
    return list(specialties)


def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
        return students
    except (FileNotFoundError, EOFError):
        return []
