import pickle
from dataclasses import dataclass
from datetime import datetime


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


def write_file(data: list[Group | Student], filename: str) -> None:
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def read_file(filename) -> list[Group | Student]:
    with open(filename, "rb") as f:
        return pickle.load(f)


def write_groups_information(groups: list[Group]) -> int:
    write_file(groups, "groups.pickle")

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    write_file(students, "students.pickle")

    return len(students)


def read_groups_information() -> list[str]:
    return list({group.specialty.name
                 for group
                 in read_file("groups.pickle")})


def read_students_information() -> list[Student]:
    return read_file("students.pickle")
