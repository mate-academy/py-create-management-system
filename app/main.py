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


def write_groups_information(groups_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups_list, groups_file)
    return max((len(group.students) for group in groups_list), default=0)


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)
    return len(students_list)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
        specialties = set(group.specialty.name for group in groups)
    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        return pickle.load(students_file)
