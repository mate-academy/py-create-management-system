import dataclasses
from datetime import datetime
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: datetime
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as p:
        pickle.dump(groups, p)
    if not groups:
        return 0
    maximum_number_of_students = max(len(group.students) for group in groups)
    return maximum_number_of_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as p:
        pickle.dump(students, p)
    number_of_students = len(students)
    return number_of_students


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as p:
        groups = pickle.load(p)
    speciality_list = [group.specialty.name for group in groups]
    return set(speciality_list)


def read_students_information() -> list:
    with open("students.pickle", "rb") as p:
        students = pickle.load(p)
    return students
