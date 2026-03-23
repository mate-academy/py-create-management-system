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


def write_groups_information(groups: list[Group]) -> int:
    number_of_students = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            number_of_students.append(len(group.students))
    if len(groups) == 0:
        return 0
    return max(number_of_students)


def write_students_information(students: list[Student]) -> int:
    student_counter = 0
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
            student_counter += 1
    return student_counter


def read_groups_information() -> list:
    groups = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                groups.append(pickle.load(file))
            except EOFError:
                break

    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break
    return students
