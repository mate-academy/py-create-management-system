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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list[str]:
    specialty_names = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialty_names.add(group.specialty.name)
            except EOFError:
                break
    return list(specialty_names)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                students.append(pickle.load(pickle_file))
            except EOFError:
                break

    return students
