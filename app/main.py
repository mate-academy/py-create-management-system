import dataclasses

from datetime import datetime

import pickle


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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)
    students_count = []
    for group in list_of_groups:
        students_count.append(len(group.students))

    if len(students_count) > 1:
        return max(students_count)
    elif len(students_count) == 1 and students_count[0] != 0:
        return students_count[0]
    return 0


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as t:
        pickle.dump(list_of_students, t)

    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as b:
        groups = pickle.load(b)

    specialities = []

    for group in groups:
        specialities.append(group.specialty.name)

    specialities = set(specialities)

    return specialities


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        student = pickle.load(f)

    return student
