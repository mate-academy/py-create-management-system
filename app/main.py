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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    result = 0

    with open("groups.pickle", "wb") as f:
        for group in groups:
            if len(group.students) > result:
                result = len(group.students)

            pickle.dump(group, f)

    return result


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> set:
    groups = []

    with open("groups.pickle", "rb") as f:
        while True:
            try:
                groups.append(pickle.load(f))
            except EOFError:
                break

    group_names = [group.specialty.name for group in groups]

    return set(group_names)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                students.append(pickle.load(f))
            except EOFError:
                break

    return students
