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
    max_students_in_groups = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            if max_students_in_groups < len(group.students):
                max_students_in_groups = len(group.students)
        pickle.dump(groups, file)

    return max_students_in_groups


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set:
    specialties = []
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        for group in groups:
            specialties.append(group.specialty.name)

    return set(specialties)


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        for student in students:
            students_list.append(student)

    return students_list
