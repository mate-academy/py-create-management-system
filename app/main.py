from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: str


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
    students: List[Student]


def write_groups_information(groups: list[Group]) -> int:
    numbers_of_students = []

    with open("groups.pickle", "wb") as file:
        for group in groups:
            numbers_of_students.append(len(group.students))
        pickle.dump(groups, file)

    return max(numbers_of_students) if numbers_of_students else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    groups_specialty_names = set()
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    for group in groups:
        groups_specialty_names.add(group.specialty.name)
    return groups_specialty_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
