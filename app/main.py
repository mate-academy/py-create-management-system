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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_group: list) -> int:
    max_student = 0
    with open("groups.pickle", "wb") as file:
        for group in list_group:
            pickle.dump(group, file)
            count_student = len(group.students)
            if count_student > max_student:
                max_student = count_student
    return max_student


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break
    return students


def read_groups_information() -> list:
    specialty_names = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialty_name = group.specialty.name
                if specialty_name not in specialty_names:
                    specialty_names.append(specialty_name)
            except EOFError:
                break
    return specialty_names
