import os.path
import pickle

from dataclasses import dataclass
from datetime import datetime
from typing import List


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
    students: List[Student]


def write_groups_information(list_of_groups: List[Group]) -> int:
    if not list_of_groups:
        return 0

    with open("groups.pickle", "wb") as file_groups_write:
        pickle.dump(list_of_groups, file_groups_write)

    return max(len(group.students) for group in list_of_groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_students_write:
        pickle.dump(students, file_students_write)

    return len(students)


def read_groups_information() -> list:
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as file_groups_read:
            groups = pickle.load(file_groups_read)

        specialty_names = list(set(group.specialty.name for group in groups))

        return specialty_names

    return []


def read_students_information() -> List[Student]:
    if os.path.exists("students.pickle"):
        with open("students.pickle", "rb") as file_students_read:
            all_students = pickle.load(file_students_read)

        all_students = [student for student in all_students]

        return all_students

    return []
