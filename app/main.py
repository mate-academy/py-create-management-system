import dataclasses
import pickle
from datetime import datetime
from typing import Any


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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> list[Any] | int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(list_of_groups, pickle_file)

    len_groups = [len(group.students) for group in list_of_groups]
    if not len_groups:
        return []
    else:
        return max(len_groups)


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_students, pickle_file)

    return len(list_of_students)


def read_groups_information() -> list[Any]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    set_specialties = {group.specialty.name for group in groups}
    return list(set_specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)

    return students
