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
    course: float
    students: list[Student]


def write_groups_information(group_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_list:
        pickle.dump(group_info, group_list)

    if not group_info:
        return 0

    max_group = max(len(group.students) for group in group_info)
    return max_group


def write_students_information(student_info: list[Student]) -> int:
    with open("students.pickle", "wb") as student_list:
        pickle.dump(student_info, student_list)

    return len(student_info)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as group_list:
        groups = pickle.load(group_list)

    specialty_names = {group.specialty.name for group in groups}
    return specialty_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as student_list:
        students = pickle.load(student_list)

    return students
