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
    course: str
    students: list


def write_groups_information(groups: list):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    amount_of_students = [len(students.students) for students in groups]
    return max(amount_of_students) if len(amount_of_students) != 0 else 0


def write_students_information(students: list):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        information = pickle.load(file)
    specialties = [i.specialty.name for i in information]
    return set(specialties)


def read_students_information():
    with open("students.pickle", "rb") as f:
        information = pickle.load(f)
    return [speciality for speciality in information]
