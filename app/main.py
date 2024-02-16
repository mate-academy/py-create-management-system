from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    students = {}
    for group in group_list:
        for student in group.students:
            students[student.first_name] = None
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)
    return len(students.keys())


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(student_list, pickle_file)
    return len(student_list)


def read_groups_information() -> list:
    specialty_list = {}
    with open("groups.pickle", "rb") as pickle_file:
        objects = pickle.load(pickle_file)
    for obj in objects:
        specialty_list[obj.specialty.name] = None
    return list(specialty_list.keys())


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        objects = pickle.load(pickle_file)
    return objects
