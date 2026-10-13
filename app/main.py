
import pickle
from dataclasses import dataclass, field
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
    students: List[Student] = field(default_factory=list)


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> List[str]:
    specialties = []

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                if group.specialty.name not in specialties:
                    specialties.append(group.specialty.name)
            except EOFError:
                break

    return specialties


def read_students_information() -> List[Student]:
    students = []

    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break

    return students
