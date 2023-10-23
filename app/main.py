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
    course: str
    students: list[Student]


def write_groups_information(groups: [Group]) -> int:

    with open("groups.pickle", "wb") as groups_pickled:
        max_students = 0

        for group in groups:
            pickle.dump(group, groups_pickled)
            if len(group.students) > max_students:
                max_students = len(group.students)

    return max_students


def write_students_information(students: [Student]) -> int:
    with open("students.pickle", "wb") as students_pickled:
        for student in students:
            pickle.dump(student, students_pickled)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_pickled:
        specialties = set()
        while True:
            try:
                group = pickle.load(groups_pickled)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return list(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_pickled:
        students = []
        while True:
            try:
                student = pickle.load(students_pickled)
                students.append(student)
            except EOFError:
                break
    return students
