import pickle
from dataclasses import dataclass
from typing import Any


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: Any
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: Any
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    students = []
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups_list, pickle_file)
    for group in groups_list:
        students.append(len(group.students))

    if students:
        return max(students)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)

    return len(students_list)


def read_groups_information() -> list[Any]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    if len(list(groups)) == 0:
        return []
    else:
        specialties = set()
        for group in groups:
            specialties.add(group.specialty.name)
        return list(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
