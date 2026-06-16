import dataclasses
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> list:
    groups = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                groups.append(pickle.load(f))
            except EOFError:
                break

    specialty_names = []
    for group in groups:
        if group.specialty.name not in specialty_names:
            specialty_names.append(group.specialty.name)
    return specialty_names


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                students.append(pickle.load(f))
            except EOFError:
                break
    return students
