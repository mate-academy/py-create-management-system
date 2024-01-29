from dataclasses import dataclass
from datetime import datetime
from pickle import dump, load


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
    all_students = []
    with open("groups.pickle", "wb") as f:
        for group in groups:
            dump(group, f)
            for student in group.students:
                if student not in all_students:
                    all_students.append(student)
    return len(all_students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            dump(student, f)
    return len(students)


def read_groups_information() -> list[str]:
    all_specialty = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = load(f)
                if group.specialty.name not in all_specialty:
                    all_specialty.append(group.specialty.name)
            except EOFError:
                break
    return all_specialty


def read_students_information() -> list[Student]:
    all_students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = load(f)
                if student not in all_students:
                    all_students.append(student)
            except EOFError:
                break
    return all_students
