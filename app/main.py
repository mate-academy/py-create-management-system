import pickle

from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:

    with open("groups.pickle", "wb") as file:
        pickle.dump(len(groups), file)
        for group in groups:
            pickle.dump(group, file)

    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:

    with open("students.pickle", "wb") as file:
        pickle.dump(len(students), file)
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list:
    result = set()

    with open("groups.pickle", "rb") as file:
        length = pickle.load(file)
        for i in range(length):
            group = pickle.load(file)
            result.add(group.specialty.name)

    return list(result)


def read_students_information() -> List[Student]:

    with open("students.pickle", "rb") as file:
        length = pickle.load(file)
        students = [pickle.load(file) for _ in range(length)]

    return students
