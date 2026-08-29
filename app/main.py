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
    course: str
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        students_number = 0
        for group in groups_list:
            pickle.dump(group, pickle_file)
            if len(group.students) > students_number:
                students_number = len(group.students)
    return students_number


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students_list:
            pickle.dump(student, pickle_file)
    return len(students_list)


def read_groups_information() -> set:
    specialties_list = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialties_list.append(group.specialty.name)
            except EOFError:
                break
    return set(specialties_list)


def read_students_information() -> list:
    student_instances_list = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                student_instances_list.append(student)
            except EOFError:
                break
    return student_instances_list
