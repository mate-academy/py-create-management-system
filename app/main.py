from dataclasses import dataclass
from typing import Union
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
    average_mark: Union[float, int]
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_groups, file)

    max_amount = 0
    for group in list_of_groups:
        if len(group.students) > max_amount:
            max_amount = len(group.students)

    return max_amount


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_of_students, file)

    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        data = [i.specialty.name for i in pickle.load(file)]
        return set(data)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
