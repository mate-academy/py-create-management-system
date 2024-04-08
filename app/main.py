import pickle
from dataclasses import dataclass
from datetime import datetime


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
    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    return max_students


def write_students_information(student: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student, file)
        return len(student)


def read_groups_information() -> str:
    names = []
    with open("groups.pickle", "rb") as file:
        data = pickle.load(file)
        for i in data:
            if i.specialty.name not in names:
                names.append(i.specialty.name)
    return names


def read_students_information() -> object:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
