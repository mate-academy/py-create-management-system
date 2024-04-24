import dataclasses

from datetime import datetime

import  pickle

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
    phone: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)
    students_count = 0
    for group in list_of_groups:
        students_count += len(group.students)

    return students_count


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as t:
        pickle.dump(list_of_students, t)

    return len(list_of_students)


def read_group_information() -> set:
    with open("groups.pickle", "rb") as b:
        groups = pickle.load(b)

    specialities = []

    for group in groups:
        specialities.append(group.specialty.name)

    specialities = set(specialities)

    return specialities


def read_students_information() -> list[Student]:
    with open("students.pickle", "rd") as f:
        student = pickle.load(f)

    return student

