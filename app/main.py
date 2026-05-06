from dataclasses import dataclass
from datetime import datetime
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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(
        groups: [Group]
) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            max_students = max(max_students, len(group.students))
            pickle.dump(group, pickle_file)
    return max_students


def write_students_information(
        students: [Student]
) -> int:
    count = 0
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            count += 1
            pickle.dump(student, pickle_file)
    return count


def read_groups_information() -> [Group]:
    specialties = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> [Student]:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                students.append(pickle.load(pickle_file))
            except EOFError:
                break
    return students
