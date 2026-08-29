from dataclasses import dataclass, field
from datetime import date
from typing import List
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student] = field(default_factory=list)


def write_groups_information(groups: List[Group]) -> int:

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:

    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> List[str]:

    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def read_students_information() -> List[Student]:

    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

    return students
