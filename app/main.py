import dataclasses
import pickle
from datetime import datetime
from typing import List


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
    students: list


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if groups:
        max_students = max([len(group.students) for group in groups])
        return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[Specialty]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialties = list(set([group.specialty.name for group in groups]))
    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
