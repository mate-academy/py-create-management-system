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


def write_groups_information(students: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(students, file)
    return max([len(group.students) for group in students], default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    ls = []
    for group in groups:
        if group.specialty.name not in ls:
            ls.append(group.specialty.name)
    return ls


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_:
        students_ls = pickle.load(file_)
    return students_ls
