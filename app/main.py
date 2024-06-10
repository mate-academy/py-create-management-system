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
    course: str
    students: list[Student]


def write_groups_information(list_of_group: list[Group]) -> int:
    with open("groups.pickle" "wb") as file:
        pickle.dump(list_of_group, file)
    return max(len(group) for group in list_of_group)


def write_students_information(list_of_student: list[Student]) -> int:
    with open("students.pickle" "wb") as file:
        pickle.dump(list_of_student, file)
    return len(list_of_student)


def read_groups_information() -> set:
    retur_set = ()
    with open("groups.pickle", "rb") as file:
        group_information = pickle.load(file)
    for group in group_information:
        retur_set.add(group.specialty)
    return retur_set


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        student_info = pickle.load(file)
    return student_info
