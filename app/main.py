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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    max_group = 0
    for group in groups:
        size_group = len(group.students)
        if size_group > max_group:
            max_group = size_group
    return max_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    list_specialty = []
    for group in groups:
        if group.specialty.name not in list_specialty:
            list_specialty.append(group.specialty.name)
    return list_specialty


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    list_students = []
    for student in students:
        list_students.append(student)
    return list_students
