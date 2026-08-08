import dataclasses
import pickle
from datetime import date
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_list, file)
        max_num_of_students = 0
        for group in groups_list:
            if len(group.students) > max_num_of_students:
                max_num_of_students = len(group.students)
    return max_num_of_students


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = set()
    for group in groups:
        specialties.add(group.specialty.name)
    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
