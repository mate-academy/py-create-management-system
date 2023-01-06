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


def write_groups_information(list_of_groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as data_to_write:
        pickle.dump(list_of_groups, data_to_write)
        max_ = 0
    for group in list_of_groups:
        if len(group.students) > max_:
            max_ = len(group.students)
    return max_


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as data_to_write:
        pickle.dump(list_of_students, data_to_write)
    return len(list_of_students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as data_to_read:
        list_of_groups = pickle.load(data_to_read)
        specials = list(set(group.specialty.name for group in list_of_groups))
    return specials


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as data_to_read:
        list_of_students = pickle.load(data_to_read)
    return list_of_students
