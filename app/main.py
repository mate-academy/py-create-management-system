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
    course: str
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_groups:
        pickle.dump(groups, file_groups)
    if groups:
        return max(len(group.students) for group in groups)
    return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        pickle.dump(students, file_students)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file_groups:
        groups = pickle.load(file_groups)
    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_students:
        students = pickle.load(file_students)
    return students
