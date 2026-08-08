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


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_list, f)
    if groups_list:
        return max(len(group.students) for group in groups_list)
    return 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)

    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        correct_info = pickle.load(f)

    return set(group.specialty.name for group in correct_info)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        correct_info = pickle.load(f)

    return correct_info
