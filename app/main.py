from dataclasses import dataclass
from datetime import datetime
import pickle
import os
from typing import List, Set


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max(map(lambda x: len(x.students), groups), default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> Set[str]:
    if not os.path.exists("groups.pickle"):
        return set()
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return {group.specialty.name for group in groups}


def read_students_information() -> List[Student]:
    if not os.path.exists("students.pickle"):
        return []
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
