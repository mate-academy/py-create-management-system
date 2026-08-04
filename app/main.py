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
    course: int | datetime
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle" , "wb") as file:
        pickle.dump(groups_list, file)
    return max((len(group.students) for group in groups_list), default=0)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> list:
    specialty_list = []
    groups_info = []
    with open("groups.pickle", "rb") as file:
        groups_info = pickle.load(file)

    for group in groups_info:
        if group.specialty.name not in specialty_list:
            specialty_list.append(group.specialty.name)
    return specialty_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_list = pickle.load(file)
    return students_list
