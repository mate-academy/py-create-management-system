import dataclasses
from datetime import datetime
import pickle
import os


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
    course: int | str
    students: list


def write_groups_information(students: list[Group]) -> int:
    if len(students) == 0:
        return
    with open("groups.pickle", "wb") as file:
        pickle.dump(students, file)
    max_students = max(len(student.students) for student in students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
        specialities = set()
        for group in groups:
            specialities.add(group.specialty.name)
        return specialities
    return set()


def read_students_information() -> str:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
