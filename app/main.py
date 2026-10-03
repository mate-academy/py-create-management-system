import pickle
from dataclasses import dataclass, field
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
    students: list[Student] = field(default_factory=list)


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list:
    specialty_names = []

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)

                if group.specialty.name not in specialty_names:
                    specialty_names.append(group.specialty.name)

            except EOFError:
                break

    return specialty_names


def read_students_information() -> list:
    students = []

    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)

            except EOFError:
                break

    return students
