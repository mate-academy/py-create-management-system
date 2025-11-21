import dataclasses
import os
import pickle

from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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


def write_groups_information(groups: list[Group]) -> int:
    if len(groups) == 0:
        return 0

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    num_of_students_in_groups = []
    for group in groups:
        num_of_students_in_groups.append(len(group.students))

    return max(num_of_students_in_groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> set[str]:
    specialties_names = set()
    if (os.path.exists("groups.pickle")
            and os.path.getsize("groups.pickle") > 0):
        with open("groups.pickle", "rb") as pickle_file:
            groups = pickle.load(pickle_file)

        for group in groups:
            specialties_names.add(group.specialty.name)

    return specialties_names


def read_students_information() -> list[Student]:
    if (os.path.exists("students.pickle")
            and os.path.getsize("students.pickle") > 0):
        with open("students.pickle", "rb") as pickle_file:
            students = pickle.load(pickle_file)

    return students
