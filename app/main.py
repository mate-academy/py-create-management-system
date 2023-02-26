from dataclasses import dataclass
from typing import List
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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if len(groups) == 0:
        return 0
    return max([len(group.students) for group in groups])


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        result = []
        for group in groups:
            result.append(group.specialty.name)
        return list(set(result))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
