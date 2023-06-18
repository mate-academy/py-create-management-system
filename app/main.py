import pickle
import dataclasses
from datetime import datetime


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        student_count = 0
        for group in groups:
            if student_count < len(group.students):
                student_count = len(group.students)
            pickle.dump(group, file)
    return student_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        specialities = []
        while True:
            try:
                group = pickle.load(pickle_file)
                if group.specialty.name not in specialities:
                    specialities.append(group.specialty.name)
            except EOFError:
                break
    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = []
        while True:
            try:
                student = pickle.load(pickle_file)
                if isinstance(student, Student):
                    students.append(student)
            except EOFError:
                break
    return students
