import dataclasses
from datetime import datetime
import pickle


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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    biggest_group = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            if len(group.students) > biggest_group:
                biggest_group = len(group.students)
            pickle.dump(group, f)

    return biggest_group


def write_students_information(students: list[Student]) -> int:
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


def read_students_information() -> list[Student]:
    all_students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
                all_students.append(student)
            except EOFError:
                break

    return all_students
