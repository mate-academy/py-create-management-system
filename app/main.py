import dataclasses
import pickle
from dataclasses import field
from datetime import datetime


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
    has_scholarship: bool = False
    phone_number: str = ""
    address: str = ""


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list = field(default_factory=list)


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
        if groups:
            return max(len(g.students) for g in groups)
        else:
            return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        specialty_names = set(g.specialty.name for g in groups)
        return specialty_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
