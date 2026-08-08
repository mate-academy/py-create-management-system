from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        max_students_count = 0
        for group in groups:
            pickle.dump(group, pickle_file)
            students_count = len(group.students)
            if max_students_count < students_count:
                max_students_count = students_count
    return max_students_count


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list:
    groups = []
    specialties = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                groups.append(group)
                specialties.add(group.specialty.name)
            except Exception:
                break
    return list(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students.append(student)
            except Exception:
                break
    return students
