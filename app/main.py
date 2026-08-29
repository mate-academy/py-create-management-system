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
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(group_list, group_file)

    if len(group_list) == 0:
        return 0

    return max(len(group.students) for group in group_list)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)

    return len(students_list)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as group_file:
        group_list = pickle.load(group_file)

    return list({group.specialty.name for group in group_list})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        students_list = pickle.load(students_file)

    return students_list
