import dataclasses
import pickle
from datetime import datetime
from typing import List


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
    students: List[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:

    with open("groups.pickle", "wb") as group_file:
        pickle.dump(list_of_groups, group_file)

    max_students = 0

    for group in list_of_groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    return max_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(list_of_students, student_file)

    return len(list_of_students)


def read_groups_information() -> list:
    list_of_specialities = []

    with open("groups.pickle", "rb") as groups_info:

        for group in pickle.load(groups_info):
            if group.specialty.name not in list_of_specialities:
                list_of_specialities.append(group.specialty.name)

    return list_of_specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_info:
        return pickle.load(students_info)
