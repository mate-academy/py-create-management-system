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


def read_all_from_pickle(filename: str) -> list:
    objects = []
    with open(filename, "rb") as f:
        while True:
            try:
                obj = pickle.load(f)
                if obj not in objects:
                    objects.append(obj)
            except EOFError:
                break

    return objects


def write_groups_information(groups: list[Group]) -> int:
    most_students = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            if len(group.students) > most_students:
                most_students = len(group.students)
            pickle.dump(group, f)
    return most_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> list:
    groups = read_all_from_pickle("groups.pickle")
    specialities = []
    for group in groups:
        if group.specialty.name not in specialities:
            specialities.append(group.specialty.name)

    return specialities


def read_students_information() -> list:
    return read_all_from_pickle("students.pickle")
