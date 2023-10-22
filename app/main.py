import pickle
from dataclasses import dataclass
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
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
    count = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            if len(group.students) > count:
                count = len(group.students)
            pickle.dump(group, file)
    return count


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> set:
    groups = []
    with open("groups.pickle", "rb") as file:
        try:
            while True:
                group = pickle.load(file)
                groups.append(group.specialty.name)
        except EOFError:
            pass
    return set(groups)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                students.append(student)
        except EOFError:
            pass
    return students
