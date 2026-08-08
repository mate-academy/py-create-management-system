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
    course: str
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_group:
        pickle.dump(group_list, file_group)
    if group_list:
        return max(len(student.students)for student in group_list)


def write_students_information(group_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file_group:
        pickle.dump(group_list, file_group)
    return len(group_list)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file_group:
        groups = pickle.load(file_group)

    speciality_uniq = list(set(group.specialty.name for group in groups))
    return speciality_uniq


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_group:
        students = pickle.load(file_group)
    return students
