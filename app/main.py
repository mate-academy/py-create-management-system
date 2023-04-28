import dataclasses
import pickle
from datetime import datetime
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_groups, file)
        max_num_of_students = 0
        for group in list_groups:
            if len(group.students) > max_num_of_students:
                max_num_of_students = len(group.students)
        return max_num_of_students


def write_students_information(list_students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_students, file)
    return len(list_students)


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
