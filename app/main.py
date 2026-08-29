import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    number_of_students = 0

    for group in groups:
        if len(group.students) > number_of_students:
            number_of_students = len(group.students)

    return number_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    groups_specialties = []
    groups: list[Group] = []

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group_in_pickle: list[Group] = pickle.load(file)
                groups += group_in_pickle
            except EOFError:
                break

    for group in groups:
        if group.specialty.name not in groups_specialties:
            groups_specialties.append(group.specialty.name)

    return groups_specialties


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student: list[Student] = pickle.load(file)
                students += student
            except EOFError:
                break

    return students
