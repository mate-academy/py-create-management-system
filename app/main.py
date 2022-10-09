from dataclasses import dataclass
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups_info: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_info, f)
    number_of_studens = [len(groups.students) for groups in groups_info]
    return max(number_of_studens) if number_of_studens else 0


def write_students_information(students_info: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_info, f)
    return len(students_info)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    groups_list = set([group.specialty.name for group in groups])
    return list(groups_list)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
