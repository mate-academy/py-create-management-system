from dataclasses import dataclass
from datetime import datetime
import pickle


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


def write_groups_information(data: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(data, pickle_file)

    return max(len(val.students) for val in data) if data else 0


def write_students_information(data: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(data, pickle_file)
    return len(data)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return sorted(list({group.specialty.name for group in groups}))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
