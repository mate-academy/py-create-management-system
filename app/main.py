from dataclasses import dataclass
from datetime import datetime
import os
import pickle


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    if not os.path.exists("groups.pickle"):
        return []

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    result = []
    for group in groups:
        specialty_name = group.specialty.name
        if specialty_name not in result:
            result.append(specialty_name)

    return result


def read_students_information() -> list[Student]:
    if not os.path.exists("students.pickle"):
        return []

    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
