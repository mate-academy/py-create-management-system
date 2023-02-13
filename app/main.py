import pickle

from dataclasses import dataclass
from datetime import datetime
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
    average_mark: int | float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group: List[Group]) -> list:
    with open("groups.pickle", "wb") as f:
        for student in group:
            pickle.dump(student, f)
    res = 0
    for group_stud in group:
        if len(group_stud.students) > res:
            res = len(group_stud.students)
    return res


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        group_list = []
        while True:
            try:
                group_list.append(pickle.load(f))
            except EOFError:
                break

    return set([group.specialty.name for group in group_list])


def read_students_information() -> List[Student]:
    student_list = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student_list.append(pickle.load(f))
            except EOFError:
                break
    return student_list
