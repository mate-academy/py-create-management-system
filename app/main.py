import pickle
from dataclasses import dataclass
from datetime import datetime
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


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students, pickle_students)

    return len(students)


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_students:
        read_students = pickle.load(pickle_students)

    return read_students


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups, pickle_groups)

    return 0 if not groups else max(len(group.students) for group in groups)


def read_groups_information() -> Set[str]:
    with open("groups.pickle", "rb") as pickle_groups:
        read_groups = pickle.load(pickle_groups)

    return set(group.specialty.name for group in read_groups)
