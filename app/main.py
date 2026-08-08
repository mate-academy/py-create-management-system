import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


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
    students: List[Student]


def write_groups_information(list_of_groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_groups, file)

    numbers_of_students = [0]
    for group in list_of_groups:
        numbers_of_students.append(len(group.students))

    return max(numbers_of_students)


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_of_students, file)

    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        list_of_groups: List[Group] = pickle.load(file)

    names_of_specialties = []
    for group in list_of_groups:
        names_of_specialties.append(group.specialty.name)

    return set(names_of_specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        list_of_students: List[Student] = pickle.load(file)

    return list_of_students
