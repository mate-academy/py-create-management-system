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


def write_groups_information(lyceum_groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as lyceum_file:
        pickle.dump(lyceum_groups, lyceum_file)
    if not lyceum_groups:
        return 0
    return max([len(group.students) for group in lyceum_groups])


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as lyceum_file:
        groups = pickle.load(lyceum_file)
    if not lyceum_file:
        return set()
    return set([group.specialty.name for group in groups])


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return students
