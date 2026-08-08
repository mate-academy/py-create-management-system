import os.path
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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: datetime.year
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    if groups:
        with open("groups.pickle", "wb") as file:
            pickle.dump(groups, file)
        return max(len(group.students) for group in groups)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as file:
            data_groups = pickle.load(file)
            specialties = [group.specialty.name for group in data_groups]
        return set(specialties)
    return {}


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        data_student = pickle.load(file)
    return [student for student in data_student]
