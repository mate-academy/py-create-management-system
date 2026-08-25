import pickle
from dataclasses import dataclass
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

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    max_students_in_groups = 0
    for group in groups:
        if len(group.students) > max_students_in_groups:
            max_students_in_groups = len(group.students)

    return max_students_in_groups


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        result = []
        for group in groups:
            result.append(group.specialty.name)

    return list(set(result))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        student = pickle.load(pickle_file)
    return student
