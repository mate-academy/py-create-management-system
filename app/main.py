from dataclasses import dataclass
import pickle
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float | int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> list[str]:
    names = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
            except EOFError:
                break
            specialty_name = group.specialty.name
            if specialty_name not in names:
                names.append(specialty_name)
    return names


def read_students_information() -> list[Student]:
    students_list = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                students_list.append(pickle.load(f))
            except EOFError:
                break
    return students_list
