import dataclasses
from typing import Optional
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
    birth_date: Optional[datetime]
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_w:
        pickle.dump(group, file_w)
    for i in group:
        return len(i.students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_w:
        pickle.dump(students, file_w)
    return len(students)


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as file_r:
        read_file = pickle.load(file_r)

    for group in read_file:
        specialties.add(group.specialty.name)

    return list(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_r:
        read_file = pickle.load(file_r)
    return read_file
