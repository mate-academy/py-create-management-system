from dataclasses import dataclass
from datetime import datetime
import pickle
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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_number_students = 0
    for group in groups:
        if len(group.students) > max_number_students:
            max_number_students = len(group.students)
    return max_number_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        info_about_groups = pickle.load(file)

    all_specialty = []
    for group in info_about_groups:
        all_specialty.append(group.specialty.name)
    return set(all_specialty)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        info_about_students = pickle.load(file)

    return info_about_students
