import pickle

from datetime import date
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in list_of_groups:
            pickle.dump(group, f)
        return max(
            [len(group.students) for group in list_of_groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as a:
        pickle.dump(students, a)
    return len(students)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as read:
        while True:
            try:
                groups = pickle.load(read)
                specialties.add(groups.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list:
    list_of_students = []
    with open("students.pickle", "rb") as read:
        while True:
            try:
                group = pickle.load(read)
                for student in group:
                    list_of_students.append(student)
            except EOFError:
                break
    return list_of_students
