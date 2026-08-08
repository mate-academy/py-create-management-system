import dataclasses
import pickle
from datetime import datetime
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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> List[str]:
    specialties: Set[str] = set()
    with open("groups.pickle", "rb") as file:
        try:
            while True:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return list(specialties)


def read_students_information() -> List[Student]:
    students: List[Student] = []
    with open("students.pickle", "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                students.append(student)
        except EOFError:
            pass
    return students
