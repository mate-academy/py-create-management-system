from datetime import datetime

import pickle
import dataclasses


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


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
    course: int | str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file_groups:
        pickle.dump(groups, file_groups)
        for group in groups:
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    num_students = len(students)
    with open("students.pickle", "wb") as file_students:
        for student in students:
            pickle.dump(student, file_students)
    return num_students


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as file_groups:
        while True:
            try:
                groups = pickle.load(file_groups)
                for group in groups:
                    specialties.add(group.specialty.name)
            except EOFError:
                break
        return specialties


def read_students_information() -> list[Student]:
    students = []

    with open("students.pickle", "rb") as file_students:
        while True:
            try:
                student = pickle.load(file_students)
                students.append(student)
            except EOFError:
                break
        return students
