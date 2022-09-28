import dataclasses
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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(lst: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(lst, file)
    return max(len(group.students) for group in lst) if lst else 0


def write_students_information(lst: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(lst, file)
    return len(lst)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = []
    for group in groups:
        if group.specialty.name not in specialties:
            specialties.append(group.specialty.name)
    return specialties


def read_students_information():
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
