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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: list[Group]) -> int:
    students_list = []
    with open("groups.pickle", "wb") as b:
        pickle.dump(groups, b)
    for group in groups:
        students_list.append(len(group.students))
    if not students_list:
        return 0
    return max(students_list)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as b:
        pickle.dump(students, b)
    return len(students)


def read_groups_information() -> list:
    specialities = []
    with open("groups.pickle", "rb") as b:
        students = pickle.load(b)
    for student in students:
        if student.specialty.name not in specialities:
            specialities.append(student.specialty.name)
    return specialities


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as b:
        students = pickle.load(b)
    for student in students:
        students_list.append(student)
    return students_list
