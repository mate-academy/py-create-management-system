import dataclasses
import pickle

from datetime import datetime
from typing import List


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
    students: List[Student]


def write_groups_information(group: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for item in group:
            pickle.dump(item, file)
        max_number_of_students = 0
        for item in group:
            if len(item.students) > max_number_of_students:
                max_number_of_students = len(item.students)
    return max_number_of_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for item in students:
            pickle.dump(item, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        results = []

        while True:
            try:
                group = pickle.load(file)
                results.append(group.specialty.name)
            except EOFError:
                break
        return list(set(results))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        results = []
        while True:
            try:
                student = pickle.load(file)
                results.append(student)
            except EOFError:
                break
        return results
