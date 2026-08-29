from dataclasses import dataclass
import pickle
from datetime import datetime


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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups, pickle_groups)

    number_of_students = []
    for group in groups:
        number_of_students.append(len(group.students))
    return max((number_of_students), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students, pickle_students)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_groups:
        groups = pickle.load(pickle_groups)
        return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_students:
        students = pickle.load(pickle_students)
        return list(students)
