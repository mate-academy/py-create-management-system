from __future__ import annotations
import dataclasses
from datetime import datetime
import pickle


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
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups_list:
            if len(group.students) > max_students:
                max_students = len(group.students)
            pickle.dump(group, file)

    return max_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)

    return len(students_list)


def read_groups_information() -> set:
    groups_specialty = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
            except EOFError:
                break
            else:
                groups_specialty.append(group.specialty.name)

    return set(groups_specialty)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return [student for student in students]
