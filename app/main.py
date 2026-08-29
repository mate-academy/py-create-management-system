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
    students_count = []
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            students_count.append(len(group.students))
    return max(students_count) if len(students_count) > 0 else 0


def write_students_information(students: list[Student]) -> int:
    students_counter = 0
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
            students_counter += 1
    return students_counter


def read_groups_information() -> list:
    students_specialty = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                students_specialty.append(pickle.load(f))
            except EOFError:
                break
    return list({group.specialty.name for group in students_specialty})


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                students.append(pickle.load(f))
            except EOFError:
                break
    return students
