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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_p:
        pickle.dump(groups, file_p)
    return (
        max([len(group.students) for group in groups])
        if groups != []
        else 0
    )


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_p:
        pickle.dump(students, file_p)
    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as file_p:
        groups = pickle.load(file_p)
    return {group.specialty.name for group in groups}


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_p:
        students = pickle.load(file_p)
    return students
