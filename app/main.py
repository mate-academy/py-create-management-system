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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_info, f)
    max_students_number = 0
    for group in group_info:
        if len(group.students) > max_students_number:
            max_students_number = len(group.students)
    return max_students_number


def write_students_information(students_info: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_info, f)
    return len(students_info)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups_info = pickle.load(f)
    return list(set([group.specialty.name for group in groups_info]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        student_info = pickle.load(f)
    return student_info
