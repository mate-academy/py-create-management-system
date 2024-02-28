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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = []
        while True:
            try:
                group = pickle.load(file)
                groups.append(group)
            except EOFError:
                break
        unique_specialties = list({group.specialty.name for group in groups})
        return unique_specialties[0]


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = []
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break
        return students[0]
