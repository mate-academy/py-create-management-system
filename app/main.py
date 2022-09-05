import dataclasses
import datetime
import pickle
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: list):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_count = []
    for students in groups:
        max_count.append(len(students.students))
    if len(max_count) != 0:
        return max(max_count)


def write_students_information(students: list):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        temp = pickle.load(file)
        name_specialty = set()
        for name in temp:
            name_specialty.add(name.specialty.name)
        return name_specialty


def read_students_information():
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
