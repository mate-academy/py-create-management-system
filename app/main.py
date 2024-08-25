import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int  # year of study
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_number = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            number_students = len(group.students)
            if number_students > max_number:
                max_number = number_students
            pickle.dump(group, f)
    return max_number


def write_students_information(students: list[Student]) -> int:
    total_students = 0
    with open("students.pickle", "wb") as f:
        for student in students:
            total_students += 1
            pickle.dump(student, f)
    return total_students


def read_groups_information() -> set[str]:
    set_groups = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
                set_groups.add(group.specialty.name)
            except EOFError:
                return set_groups


def read_students_information() -> list[Student]:
    list_students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
                list_students.append(student)
            except EOFError:
                return list_students
