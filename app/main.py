# write your code here
import os
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    speciality: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        return 0

    with open("groups.pickle", "wb") as handle:
        pickle.dump(groups, handle)

    max_student = max(len(group.students) for group in groups)
    return max_student


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as handle:
        pickle.dump(students, handle)
    return len(students)


def read_groups_information() -> set:
    if not os.path.exists("groups.pickle"):
        return set()
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return {group.specialty.name for group in groups}


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as handle:
        students = pickle.load(handle)
    return students
