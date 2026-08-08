from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List


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
    course: float
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_number_of_students = 0

    with open("groups.pickle", "wb") as file:
        for group in groups:

            pickle.dump(group, file)
            if len(group.students) > max_number_of_students:
                max_number_of_students = len(group.students)

    return max_number_of_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)

    return len(students)


def read_groups_information() -> set:
    res = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                res.append(pickle.load(file).specialty.name)
            except Exception:
                break

    return set(res)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        res = []
        while True:
            try:
                res.append(pickle.load(file))
            except Exception:
                break

    return res
