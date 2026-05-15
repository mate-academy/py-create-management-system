from dataclasses import dataclass
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
    birth_date: object
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
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            if group.students is not None:
                max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> List[str]:
    specialties = []
    seen = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                except EOFError:
                    break
                name = getattr(group.specialty, "name", None)
                if name is not None and name not in seen:
                    seen.add(name)
                    specialties.append(name)
    except FileNotFoundError:
        return []
    return specialties


def read_students_information() -> List[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student = pickle.load(f)
                except EOFError:
                    break
                students.append(student)
    except FileNotFoundError:
        return []
    return students
