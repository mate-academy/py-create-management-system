import dataclasses
import pickle
from datetime import datetime
from typing import List


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
    maximal_students_count = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            maximal_students_count = max(len(group.students),
                                         maximal_students_count)
    return maximal_students_count


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
            except EOFError:
                return sorted(specialties)


def write_students_information(students: List[Student]) -> int:
    total_students = 0
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
            total_students += 1
    return total_students


def read_students_information() -> List[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                return students
