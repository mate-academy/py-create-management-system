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
    specialty: type
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file:  # open file in write-binary mode
        for group in groups:
            pickle.dump(group, file)
    if groups:
        return max(len(g.students) for g in groups)
    else:
        return 0


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list:
    names = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
                names.add(group.specialty.name)
            except EOFError:
                break
    return list(names)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:

        while True:
            try:
                student = pickle.load(f)
                students.append(student)
            except EOFError:
                break

    return students
