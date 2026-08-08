from dataclasses import dataclass
from typing import List

from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(all_groups: List[Group]) -> int:
    max_number_of_students = 0
    for item in all_groups:
        if len(item.students) > max_number_of_students:
            max_number_of_students = len(item.students)
    with open("groups.pickle", "wb") as f:
        pickle.dump(all_groups, f)
    return max_number_of_students


def write_students_information(all_students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(all_students, f)
    return len(all_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        lyceum = pickle.load(f)
    return {item.specialty.name for item in lyceum}


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return [student for student in students]
