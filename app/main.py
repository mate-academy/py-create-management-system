import pickle

from dataclasses import dataclass
from datetime import datetime
from typing import List


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    if groups:
        max_students = max(len(group.students) for group in groups)
        return max_students
    else:
        return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as pickle_file:
        specialty_groups = pickle.load(pickle_file)
        specialty_names = set(
            group.specialty.name for group in specialty_groups)
        return list(specialty_names)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
        return students
