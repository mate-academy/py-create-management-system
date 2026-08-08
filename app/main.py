from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as output_file:
        pickle.dump(students, output_file)
    return len(students)


def write_groups_information(groups: list[Group]) -> int:
    max_count_of_students = 0
    with open("groups.pickle", "wb") as output_file:
        pickle.dump(groups, output_file)
        for group in groups:
            if max_count_of_students < len(group.students):
                max_count_of_students = len(group.students)
    return max_count_of_students


def read_groups_information() -> list:
    dictionary = {}
    with open("groups.pickle", "rb") as input_file:
        groups = pickle.load(input_file)
        for group in groups:
            name_of_specialty = group.specialty.name
            dictionary[name_of_specialty] = name_of_specialty
        return [key for key in dictionary.keys()]


def read_students_information() -> list:
    with open("students.pickle", "rb") as input_file:
        return list(pickle.load(input_file))
