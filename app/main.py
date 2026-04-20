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
    students: list


def read_students_information():
    with open("students.pickle", "rb") as f:
        data = pickle.load(f)
    return data


def write_students_information(students_list):
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)

