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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    count_students = []
    for group in groups:
        count_students.append(len(group.students))
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max(count_students, default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    name_groups = set()
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    for group in groups:
        name_groups.add(group.specialty.name)
    return name_groups


def read_students_information() -> list:
    list_students = []
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    for student in students:
        list_students.append(student)
    return list_students
