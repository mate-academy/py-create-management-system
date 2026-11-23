"""Data models and persistence helpers for the lyceum management system."""

import pickle
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Union


@dataclass
class Specialty:
    """A study specialty offered by the lyceum."""

    name: str
    number: int


@dataclass
class Student:
    """Information about a student."""

    first_name: str
    last_name: str
    birth_date: Union[date, datetime]
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    """A group of students studying a specialty in a given course."""

    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    """Save groups and return the largest group's student count."""
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    """Save each student to one pickle stream and return their count."""
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> List[str]:
    """Read groups and return specialty names without duplicates."""
    specialty_names = []
    seen_names = set()

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
            except EOFError:
                break

            name = group.specialty.name
            if name not in seen_names:
                seen_names.add(name)
                specialty_names.append(name)

    return specialty_names


def read_students_information() -> List[Student]:
    """Read and return all students from the pickle stream."""
    students = []

    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break

    return students
