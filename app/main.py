from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List, Set


@dataclass
class Specialty:
    name: str
    number: str


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
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
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> Set[str]:
    specialties_names = set()
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                try:
                    group = pickle.load(file)
                    specialties_names.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return specialties_names


def read_students_information() -> List[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                try:
                    student = pickle.load(file)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return students
