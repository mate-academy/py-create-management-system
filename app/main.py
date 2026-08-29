import pickle
from datetime import datetime
from dataclasses import dataclass


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
    with open("groups.pickle", "wb") as f:
        max_students = 0
        for group in groups:
            pickle.dump(group, f)

            current_count = len(group.students)

            if current_count > max_students:
                max_students = current_count

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list:
    specialty_names = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
                specialty_names.add(group.specialty.name)
            except EOFError:
                break
    return list(specialty_names)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_list = []
        while True:
            try:
                student = pickle.load(file)
                students_list.append(student)
            except EOFError:
                break

    return students_list
