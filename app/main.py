from dataclasses import dataclass
from datetime import datetime, date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information():
    pass


def write_students_information():
    pass


def read_groups_information():
    pass


def read_students_information():
    pass
