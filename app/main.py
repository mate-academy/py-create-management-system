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
    course: datetime
    students: Student


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if len(groups) > 0:
        students_group = []
        for group in groups:
            students_group.append(len(group.students))
        return max(students_group)
    else:
        return 0


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = set()
    for group in groups:
        specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
