import dataclasses
import pickle

from datetime import datetime


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
    students: list[Student]


def write_groups_information(groups_data: list[Group]) -> int:
    max_number_of_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups_data:
            pickle.dump(group, file)
            if max_number_of_students < len(group.students):
                max_number_of_students = len(group.students)
    return max_number_of_students


def write_students_information(students_data: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students_data:
            pickle.dump(student, file)
    return len(students_data)


def read_groups_information() -> list[str]:
    specialties = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                if group.specialty.name not in specialties:
                    specialties.append(group.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list[Student]:
    students_data = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students_data.append(student)
            except EOFError:
                break
    return students_data
