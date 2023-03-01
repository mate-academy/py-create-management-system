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


def write_groups_information(group_info: List[Group]) -> int:
    with open("groups.pickle", "wb") as converted_group_info:
        pickle.dump(group_info, converted_group_info)
    if group_info:
        return max([len(group.students) for group in group_info])
    return 0


def write_students_information(students_info: List[Student]) -> int:
    with open("students.pickle", "wb") as converted_students_info:
        pickle.dump(students_info, converted_students_info)
    return len(students_info)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as group_info:
        group = pickle.load(group_info)
    return set(person.specialty.name for person in group)


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_info:
        group = pickle.load(students_info)
    return group
