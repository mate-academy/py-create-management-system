from typing import List
from datetime import datetime
from dataclasses import dataclass
import pickle


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_students = 0
    for group in groups:
        num_students = len(group.students)
        if num_students > max_students:
            max_students = num_students

    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    quantity_students = len(students)

    return quantity_students


def read_groups_information(groups_file: str = "groups.pickle") -> list:
    with open(groups_file, "rb") as f:
        groups_data = pickle.load(f)

    uniq_specialties = []
    for group in groups_data:
        if group.specialty.name not in uniq_specialties:
            uniq_specialties.append(group.specialty.name)

    return uniq_specialties


def read_students_information(
        students_file: str = "students.pickle"
) -> List[Student]:
    with open(students_file, "rb") as f:
        students_data = pickle.load(f)

    return students_data
