from dataclasses import dataclass
from datetime import datetime
import pickle


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
    students: list


def write_groups_information(group: list) -> int:
    with open("groups.pickle", "wb") as f:
        for item in group:
            pickle.dump(item, f)

    if not group:
        return 0

    return max(len(item.students) for item in group)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> list:
    specialties = []

    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)

                if group.specialty.name not in specialties:
                    specialties.append(group.specialty.name)

            except EOFError:
                break

    return specialties


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                students.append(pickle.load(f))
            except EOFError:
                break
    return students
