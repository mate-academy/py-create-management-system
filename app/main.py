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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: "Specialty"
    course: int
    students: List["Student"]


def write_groups_information(groups: List["Group"]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
    return max((len(g.students) for g in groups), default=0)


def write_students_information(students: List["Student"]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> List[str]:
    specialty_names: List[str] = []
    try:
        with open("groups.pickle", "rb") as pickle_file:
            while True:
                try:
                    group = pickle.load(pickle_file)
                except EOFError:
                    break
                name = group.specialty.name
                if name not in specialty_names:
                    specialty_names.append(name)
    except FileNotFoundError:
        return []
    return specialty_names


def read_students_information() -> List["Student"]:
    students: List[Student] = []
    try:
        with open("students.pickle", "rb") as pickle_file:
            while True:
                try:
                    student = pickle.load(pickle_file)
                except EOFError:
                    break
                students.append(student)
    except FileNotFoundError:
        return []
    return students
