import pickle
import dataclasses
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_with_groups: list[Group]) -> int:
    max_students = 0
    for group in list_with_groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_with_groups, f)
    return max_students


def write_students_information(list_with_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_with_students, file)
    return len(list_with_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        list_with_groups = pickle.load(file)
    specialties = []
    for group in list_with_groups:
        specialties.append(group.specialty.name)
    return set(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        list_with_students = pickle.load(file)
    return list_with_students
