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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: Student


def write_groups_information(groups: list):
    try:
        with open("groups.pickle", "wb") as file:
            pickle.dump(groups, file)
        if len(groups) == 0:
            return 0
        return max(len(group.students) for group in groups)
    except FileNotFoundError:
        return "No such file or directory"


def write_students_information(students: list):
    try:
        with open("students.pickle", "wb") as file:
            pickle.dump(students, file)
        return len(students)
    except FileNotFoundError:
        return "No such file or directory"


def read_groups_information():
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
        return {group.specialty.name for group in groups}
    except FileNotFoundError:
        return "No such file or directory"


def read_students_information():
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
        return students
    except FileNotFoundError:
        return "No such file or directory"
