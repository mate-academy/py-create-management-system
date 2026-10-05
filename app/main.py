import dataclasses
from datetime import date, datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date | datetime
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
    with open("groups.pickle", "wb") as output:
        for group in groups:
            pickle.dump(group, output)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as output:
        for student in students:
            pickle.dump(student, output)
    return len(students)


def read_groups_information() -> list[str]:
    specialties = []
    with open("groups.pickle", "rb") as source:
        while True:
            try:
                group = pickle.load(source)
            except EOFError:
                break
            if group.specialty.name not in specialties:
                specialties.append(group.specialty.name)
    return specialties


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as source:
        while True:
            try:
                students.append(pickle.load(source))
            except EOFError:
                break
    return students
