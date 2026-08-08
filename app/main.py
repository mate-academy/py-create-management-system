import pickle
from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    return max(map(len, [group.students for group in groups]), default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

    group_specialty = {group.specialty.name for group in groups}

    return sorted(group_specialty)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)

    return students
