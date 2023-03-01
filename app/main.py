import dataclasses
from datetime import datetime
import pickle


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            max_students = max(max_students, len(group.students))
        return max_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
        return len(students)


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return list(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
                students.append(student)
            except EOFError:
                break
    return students
