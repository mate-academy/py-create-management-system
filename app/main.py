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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as data_file:
        pickle.dump(groups, data_file)

    max_students = 0
    for group in groups:
        if max_students < len(group.students):
            max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as data_file:
        pickle.dump(students, data_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as data_file:
        groups = pickle.load(data_file)
    all_specialty = [group.specialty.name for group in groups]
    return set(all_specialty)


def read_students_information() -> list:
    with open("students.pickle", "rb") as data_file:
        students = pickle.load(data_file)
    return students
