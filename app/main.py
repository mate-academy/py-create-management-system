import pickle
from dataclasses import dataclass
from datetime import datetime


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
        for group in groups:
            pickle.dump(group, file)

    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if isinstance(data, list):
                    for group in data:
                        specialties.add(group.specialty.name)
                else:
                    specialties.add(data.specialty.name)
            except EOFError:
                break

        return list(specialties)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if isinstance(data, list):
                    students.extend(data)
                else:
                    students.append(data)
            except EOFError:
                break
    return students
