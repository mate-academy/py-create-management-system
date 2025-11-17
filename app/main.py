import dataclasses
from datetime import datetime
import pickle
from typing import List, Set


# -------------------
# Класи
# -------------------

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
    students: List[Student]


# -------------------
# Функції
# -------------------

def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    max_students = max(len(group.students)
                       for group in groups) if groups else 0
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> Set[str]:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group: Group = pickle.load(f)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return specialties


def read_students_information() -> List[Student]:
    """Читає студентів з 'students.pickle' та повертає список Student."""
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student: Student = pickle.load(f)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return students
