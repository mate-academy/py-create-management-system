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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = 0

    for group in groups:
        students_count = len(group.students)

        if students_count > max_students:
            max_students = students_count

    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file:
        groups: List[Group] = pickle.load(file)

    specialties: List[str] = []

    for group in groups:
        name = group.specialty.name

        if name not in specialties:
            specialties.append(name)

    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students: List[Student] = pickle.load(file)

    return students
