from dataclasses import dataclass
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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    if groups:
        return len(max(groups, key=lambda item: len(item.students)).students)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[Specialty]:
    lst = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                item = pickle.load(file)
                lst.append(item)
            except EOFError:
                break
    return list(set([i.specialty.name for i in lst]))


def read_students_information() -> list[Student]:
    lst = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                item = pickle.load(file)
                lst.append(item)
            except EOFError:
                break
    return lst
