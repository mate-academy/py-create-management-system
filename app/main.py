import dataclasses
from datetime import datetime
import pickle
from typing import List, Set


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> Set[str]:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        try:
            while True:
                group = pickle.load(f)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return specialties


def read_students_information() -> List[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            try:
                while True:
                    student = pickle.load(f)
                    students.append(student)
            except EOFError:
                pass
    except FileNotFoundError:
        print("File 'students.pickle' not found.")
    return students
