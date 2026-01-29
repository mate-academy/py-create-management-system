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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file:
        max_size_group = 0
        for group in groups:
            if max_size_group < len(group.students):
                max_size_group = len(group.students)
        pickle.dump(groups, file)
    return max_size_group


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_students_information() -> list:
    list_students = []
    with open("students.pickle", "rb") as file:
        tmp = pickle.load(file)
        for student in tmp:
            list_students.append(student)
    return list_students


def read_groups_information() -> list:
    list_speciality = []
    with open("groups.pickle", "rb") as file:
        tmp = pickle.load(file)
        for group in tmp:
            if group.specialty.name not in list_speciality:
                list_speciality.append(group.specialty.name)
    return list_speciality
