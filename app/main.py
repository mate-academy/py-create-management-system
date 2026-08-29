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
    max_number_of_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
            max_number_of_students = max(max_number_of_students,
                                         len(group.students))
    return max_number_of_students


def write_students_information(students: list[Student]) -> int:
    number_of_students = 0
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
            number_of_students += 1
    return number_of_students


def read_groups_information() -> list:
    groups_specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                groups_specialties.append(group.specialty.name)
            except EOFError:
                break
    return sorted(set(groups_specialties))


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students_list.append(student)
            except EOFError:
                break
    return students_list
