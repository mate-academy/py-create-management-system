from datetime import datetime
import dataclasses
import pickle
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
    average_mark : float
    has_scholarship: bool
    phone_number: str
    address : str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course : int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(list_of_groups, pickle_file)

    if not list_of_groups:
        return 0

    max_students = max(len(group.students) for group in list_of_groups)

    return max_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_students, pickle_file)

    return len(list_of_students)


def read_groups_information() -> set[Any]:
    with open("groups.pickle", "rb") as pickle_file:
        list_of_groups = pickle.load(pickle_file)

    names_of_specialty = []
    for group in list_of_groups:
        names_of_specialty.append(group.specialty.name)

    return set(names_of_specialty)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        list_of_students = pickle.load(pickle_file)

    return list_of_students
