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
    phone_number: int | str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as g:
        pickle.dump(groups, g)
    if len(groups) == 0:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as s:
        pickle.dump(students, s)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as g:
        groups = pickle.load(g)
        return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as s:
        students = pickle.load(s)
    return students
