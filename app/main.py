import dataclasses
from datetime import datetime
import pickle
import os


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


def write_groups_information(list_of_groups: list[Group]) -> int:
    number_of_students = 0
    if len(list_of_groups) == 0:
        return 0

    for group in list_of_groups:
        if number_of_students < len(group.students):
            number_of_students = len(group.students)

    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_groups, file)

    return number_of_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_of_students, file)

    return len(list_of_students)


def read_groups_information() -> list[Group]:
    if not os.path.exists("groups.pickle"):
        return []

    with open("groups.pickle", "rb") as file:
        list_of_groups = pickle.load(file)

        if list_of_groups is None:
            return []

        group_specialites_names = []
        for group in list_of_groups:
            group_specialites_names.append(group.specialty.name)

        group_specialites_names = list(set(group_specialites_names))

        return group_specialites_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        list_of_students = pickle.load(file)

        return list_of_students
