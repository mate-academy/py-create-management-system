from dataclasses import dataclass
from datetime import datetime
import pickle
import os


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def loadall(filename: str) -> None:
    with open(filename, "rb") as my_file:
        while True:
            try:
                yield pickle.load(my_file)
            except EOFError:
                break


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as my_file:
        pickle.dump(groups, my_file)
        if groups:
            return max([len(group.students) for group in groups])
        return []


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as my_file:
        pickle.dump(students, my_file)
    return len(students)


def read_groups_information() -> list:
    specialties_names = []
    if os.path.isfile("groups.pickle"):
        items = loadall("groups.pickle")
    for item in items:
        for group in item:
            specialties_names.append(group.specialty.name)
    return list(set(specialties_names))


def read_students_information() -> list:
    students = []
    if os.path.isfile("students.pickle"):
        items = loadall("students.pickle")
        for item in items:
            for student in item:
                students.append(student)
    return students
