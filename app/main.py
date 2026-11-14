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
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_all(file_name: str) -> list:
    items = []
    with open(file_name, "rb") as file:
        while True:
            try:
                items.append(pickle.load(file))
            except EOFError:
                return items


def read_groups_information() -> list[str]:
    groups = read_all("groups.pickle")
    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    return read_all("students.pickle")
