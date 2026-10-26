from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List, Set


@dataclass
class Specialty:
    name: str
    number: str


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> Set[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups: List[Group] = pickle.load(file)
    except (FileNotFoundError, EOFError):
        return set()

    specialty_names = {group.specialty.name for group in groups}
    return specialty_names


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students: List[Student] = pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

    return students
