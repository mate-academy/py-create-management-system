import dataclasses
import pickle
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
    students: Student


def write_groups_information(groups: list) -> int:
    num_of_students = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    for group in groups:
        if len(group.students) > num_of_students:
            num_of_students += len(group.students)
    return num_of_students


def write_students_information(students: list) -> int:
    num_students = len(students)
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return num_students


def read_groups_information() -> list:
    specialty_name_list = []
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        for group in groups:
            if group.specialty.name not in specialty_name_list:
                specialty_name_list.append(group.specialty.name)
    return specialty_name_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
