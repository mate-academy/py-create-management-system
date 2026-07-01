import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name : str
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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0
    return max(len(g.students) for g in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    if not students:
        return 0
    return len(students)


def read_groups_information() -> set | list:
    try:
        with open("groups.pickle", "rb") as f:
            data_groups = pickle.load(f)
    except FileNotFoundError:
        return []
    return {group.specialty.name for group in data_groups}


def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []
