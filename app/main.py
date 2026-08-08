from dataclasses import dataclass
from typing import List
import os
from pickle import load, dump


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
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

    if not groups:
        return 0

    with open("groups.pickle", "wb") as file_of_groups:
        for group in groups:
            dump(group, file_of_groups)
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_of_students:
        dump(students, file_of_students)
    return len(students)


def read_groups_information() -> list:
    specialty = set()
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as read_groups:
            while True:
                try:
                    group = load(read_groups)
                    specialty.add(group.specialty.name)
                except EOFError:
                    break

    return list(specialty)


def read_students_information() -> List[Student]:
    students = []
    with open("students.pickle", "rb") as read_students:
        while True:
            try:
                student = load(read_students)
                students.append(student)
            except EOFError:
                break

    return students[0]
