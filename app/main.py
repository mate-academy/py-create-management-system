from __future__ import annotations

from dataclasses import dataclass
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
    students: [Student]


def write_groups_information(all_groups: list) -> int:
    with open("groups.pickle", "wb") as groups:
        pickle.dump(all_groups, groups)
        result = []
        for group in all_groups:
            for student in group.students:
                if student not in result:
                    result.append(student)
        return len(result)


def write_students_information(students: [Student]) -> int:
    with open("students.pickle", "wb") as student:
        pickle.dump(students, student)
        return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as text:
        groups = pickle.load(text)
        return set(group.specialty.name for group in groups)


def read_students_information() -> [Student]:
    with open("students.pickle", "rb") as students:
        return pickle.load(students)
