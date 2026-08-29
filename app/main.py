import dataclasses
import pickle
from datetime import datetime


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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_list, file)

    max_students_amount = 0
    for group in groups_list:
        group_size = len(group.students)
        if group_size > max_students_amount:
            max_students_amount = group_size

    return max_students_amount


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)

    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups_list = pickle.load(file)

    specialties_names = set()
    for group in groups_list:
        specialties_names.add(group.specialty.name)

    return specialties_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students_list = pickle.load(file)

    return students_list
