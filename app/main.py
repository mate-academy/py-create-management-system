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


def write_groups_information(groups: object) -> int:
    count = 0
    with open("groups.pickle", "wb") as file:
        for index in range(len(groups)):
            pickle.dump(groups[index], file)
    for index in range(len(groups)):
        if len(groups[index].students) > 0:
            count += len(groups[index].students)
        return count


def write_students_information(students: object) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        try:
            while True:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return specialties


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                students.append(student)
        except EOFError:
            pass
    return students
