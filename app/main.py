import pickle
from dataclasses import dataclass
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
    maxe = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            if len(group.students) > maxe:
                maxe = len(group.students)

    return maxe


def write_students_information(lads: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in lads:
            pickle.dump(student, f)

        return len(lads)


def read_groups_information() -> list:
    specialties = set()

    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
                specialties.add(group.specialty.name)
            except EOFError:
                break

    return list(specialties)


def read_students_information() -> list:
    lilist = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
                lilist.append(student)
            except EOFError:
                break
    return lilist
