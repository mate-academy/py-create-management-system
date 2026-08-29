import dataclasses
from datetime import datetime
from typing import List
import pickle


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    """
    Write groups information to "groups.pickle".
    Returns max number of students in any group.
    """
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    """
    Write students information to "students.pickle".
    Returns total number of students.
    """
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> List[str]:
    """
    Read data from "groups.pickle".
    Returns list of unique specialty names.
    """
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

    specialties = set()
    for group in groups:
        specialties.add(group.specialty.name)

    return list(specialties)


def read_students_information() -> List[Student]:
    """
    Read data from "students.pickle".
    Returns list of Student instances.
    """
    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

    return students
