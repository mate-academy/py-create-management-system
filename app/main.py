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
    average_mark: int
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    students = 0
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
        for group in groups:
            if len(group.students) > students:
                students = len(group.students)
    return students


def write_students_information(list_of_students: list[Student]) -> int:
    students = len(list_of_students)
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_students, pickle_file)
    return students


def read_groups_information() -> list:
    groups_list_unique_specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        for group in groups:
            if group.specialty.name not in groups_list_unique_specialties:
                groups_list_unique_specialties.append(group.specialty.name)
    return groups_list_unique_specialties


def read_students_information() -> list:
    student_instances = []
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
        for student in students:
            student_instances.append(student)

    return student_instances
