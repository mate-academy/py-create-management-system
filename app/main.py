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
    average_mark : float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)

    if not group_list:
        return 0
    return max(len(group.students) for group in group_list)


def write_students_information(studens_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(studens_list, pickle_file)

    return len(studens_list)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
