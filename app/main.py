from dataclasses import dataclass, field
from datetime import datetime
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
    birth_date: datetime
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
    """Write groups to pickle and return max number of students."""
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    """Write all students to pickle and return their count."""
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> List[str]:
    """Return list of specialty names without duplicates."""
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    names = {group.specialty.name for group in groups}
    return list(names)


def read_students_information() -> List[Student]:
    """Return list of all students from pickle."""
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
