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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    students = []
    for group in groups:
        for student in group.students:
            if student not in students:
                students.append(student)
    return len(students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        result = len(students)
    return result


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        readed_file = pickle.load(f)
        specialties = []
        for group in readed_file:
            if group.specialty.name not in specialties:
                specialties.append(group.specialty.name)
        return specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        readed_file = pickle.load(f)
        return readed_file
