from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty :
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
    Specialty : Specialty 
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> set[str]:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as pickle_file:
            while True:
                try:
                    group = pickle.load(pickle_file)
                    specialties.add(group.Specialty .name)
                except EOFError:
                    break
    except FileNotFoundError:
        return set()
    return specialties


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as pickle_file:
            while True:
                try:
                    student = pickle.load(pickle_file)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return students
