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


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        count = 0
        for student in students:
            count += 1
            pickle.dump(student, file)
        return count


def write_groups_information(groups: list[Group]) -> int:
    max_number = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            if len(group.students) > max_number:
                max_number = len(group.students)
    return max_number


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
            except EOFError:
                break
            students.append(student)
    return students


def read_groups_information() -> list[str]:
    specialty = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                if group.specialty.name not in specialty:
                    specialty.append(group.specialty.name)
            except EOFError:
                break
    return specialty
