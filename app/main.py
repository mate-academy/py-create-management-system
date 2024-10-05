from dataclasses import dataclass
from datetime import datetime
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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_info:
        pickle.dump(groups, groups_info)

    if len(groups) == 0:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_info:
        pickle.dump(students, students_info)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_info:
        groups = pickle.load(groups_info)

    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_info:
        students = pickle.load(students_info)

    return students
