from dataclasses import dataclass
from datetime import date
from typing import List
import pickle


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


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups_info: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_info, file)
    max_count = 0
    for group in groups_info:
        if len(group.students) > max_count:
            max_count = len(group.students)
    return max_count


def write_students_information(students_info: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_info, file)
    return len(students_info)


def read_groups_information() -> set:
    list_of_specialties = []
    with open("groups.pickle", "rb") as file:
        groups_info = pickle.load(file)
    for group in groups_info:
        list_of_specialties.append(group.specialty.name)
    return set(list_of_specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_info = pickle.load(file)
    return students_info
