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
    students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
            if len(group.students) > students:
                students = len(group.students)
    return students


def write_students_information(list_of_students: list[Student]) -> int:
    students = len(list_of_students)
    with open("students.pickle", "wb") as pickle_file:
        for student in list_of_students:
            pickle.dump(student, pickle_file)
    return students


def read_groups_information() -> list[str]:
    groups_list_unique_specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                if group.specialty.name not in groups_list_unique_specialties:
                    groups_list_unique_specialties.append(group.specialty.name)
            except EOFError:
                break

    return groups_list_unique_specialties


def read_students_information() -> list[Student]:
    student_instances = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                student_instances.append(student)
            except EOFError:
                break

    return student_instances
