import pickle

from dataclasses import dataclass

from datetime import date

from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: List[Specialty]
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    users_list = []
    for user in groups:
        users_list.append(len(user.students))
    if not users_list:
        return 0
    return max(users_list)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        data = pickle.load(file)
    speciality_name = [user.specialty.name for user in data]
    return set(speciality_name)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        data = pickle.load(file)
    return [user for user in data]
