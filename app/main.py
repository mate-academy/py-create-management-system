from dataclasses import dataclass
from datetime import datetime
from typing import List
import pickle


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


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        return 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    return max(len(group.students) for group in groups)


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
        print("The file 'groups.pickle' does not exist.")
    return list(specialties)


def read_students_information() -> List[Student]:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
                students.append(student)
            except EOFError:
                break
    return students
