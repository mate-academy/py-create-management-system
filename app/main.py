import dataclasses
import pickle
from typing import List
from datetime import date


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    max_students = 0
    for i in groups:
        if len(i.students) > max_students:
            max_students = len(i.students)

    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> List[str]:
    specialties = set()
    groups = []

    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    groups.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    for i in groups:
        specialties.add(i.specialty.name)

    return list(specialties)


def read_students_information() -> List[Student]:
    students = []

    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    students.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return students
