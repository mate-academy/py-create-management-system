import dataclasses
from datetime import datetime
import pickle
from typing import List, Set


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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> Set[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
        return {group.specialty.name for group in groups}
    except (FileNotFoundError, EOFError):
        return set()


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []
