from dataclasses import dataclass
from datetime import date
import pickle


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for groups in group_list:
            pickle.dump(groups, file)
    if group_list:
        return len(
            max(group_list, key=lambda group: len(group.students)).students
        )
    return 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students_list:
            pickle.dump(student, file)

    return len(students_list)


def read_groups_information() -> list[str]:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                specialties.add(pickle.load(file).specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break
    return students
