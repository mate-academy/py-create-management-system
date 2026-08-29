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
    with open("groups.pickle", "wb") as file:
        max_students = 0
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
            pickle.dump(group, file)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as file:
        names = []
        while True:
            try:
                group = pickle.load(file)
                names.append(group.specialty.name)
            except EOFError:
                break
        names = set(names)
    return names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        list_of_students = []
        while True:
            try:
                student = pickle.load(file)
                list_of_students.append(student)
            except EOFError:
                break
    return list_of_students
