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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    return max(
        [len(group.students) for group in groups]
    ) if groups != [] else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list:
    specialties_of_group = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    for group in groups:
        specialties_of_group.append(group.specialty.name)
    return list(set(specialties_of_group))


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                students.append(pickle.load(pickle_file))
            except EOFError:
                break
    return students
