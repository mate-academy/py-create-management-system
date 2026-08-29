from dataclasses import dataclass, field
import datetime
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
    birth_date: datetime.date
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


def read_groups_information() -> Set[str]:
    try:
        with open("groups.pickle", "rb") as f:
            groups: List[Group] = pickle.load(f)
    except (FileNotFoundError, EOFError):
        return set()

    return {group.specialty.name for group in groups}


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as f:
            students: List[Student] = pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

    return students
