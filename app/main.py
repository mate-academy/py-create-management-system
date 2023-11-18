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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(inf: list[Group]) -> int:
    students_digit = []
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(inf, pickle_file)
        for group in inf:
            students_digit.append(len(group.students))
    return students_digit and max(students_digit)


def write_students_information(inf: list[Student]) -> int:
    students_digit = 0
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(inf, pickle_file)
        for group in inf:
            students_digit += len(inf)
    return len(inf)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
