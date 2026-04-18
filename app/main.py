import pickle
from dataclasses import dataclass, field
from datetime import datetime
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
    specialty: Specialty
    course: int
    students: List[Student] = field(default_factory=list)


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    # Повертаємо максимальну кількість студентів серед усіх груп
    return max((len(g.students) for g in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> List[str]:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return sorted(list(specialties))


def read_students_information() -> List[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student = pickle.load(f)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return students
