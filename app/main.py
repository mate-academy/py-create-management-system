import dataclasses
from datetime import datetime
import pickle


@dataclasses
class Specialty:
    name: str
    number: int


@dataclasses
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_group_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
        for group in groups:
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    groups_specialties = set()
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        for group in groups:
            groups_specialties.add(group.specialty.name)
    return groups_specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
