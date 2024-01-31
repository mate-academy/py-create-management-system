import pickle
from dataclasses import dataclass
from datetime import date


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


def write_groups_information(group_ls: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_ls, file)
    students_number = 0
    for group in group_ls:
        if students_number < len(group.students):
            students_number = len(group.students)

    return students_number


def write_students_information(students_ls: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_ls, file)
    return len(students_ls)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = []

    for group in groups:
        specialties.append(group.specialty.name)

    return set(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    students_ls = []
    for student in students:
        students_ls.append(student)

    return students_ls
