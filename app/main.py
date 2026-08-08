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
    result = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            if len(group.students) > result:
                result = len(group.students)
    return result


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        specialties = []
        while True:
            try:
                current_group = pickle.load(f)
                specialties.append(current_group.specialty.name)
            except EOFError:
                break
    return set(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        result = []
        while True:
            try:
                result.append(pickle.load(f))
            except EOFError:
                break
    return result
