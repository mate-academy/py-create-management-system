from datetime import datetime
from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int | None:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    if groups:
        return max(len(group.students) for group in groups)
    return None


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = []
        while 1:
            try:
                groups.append(pickle.load(file))
            except EOFError:
                return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = []
        while 1:
            try:
                students.append(pickle.load(file))
            except EOFError:
                return students
