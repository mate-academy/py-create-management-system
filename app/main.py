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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    max_students_in_group = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            if len(group.students) > max_students_in_group:
                max_students_in_group = len(group.students)
            pickle.dump(group, pickle_file)
    return max_students_in_group


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        num_of_students = len(student_list)
        for student in student_list:
            pickle.dump(student, pickle_file)
    return num_of_students


def read_groups_information() -> list[Specialty]:
    specialty_list = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                specialty_list.append(pickle.load(pickle_file).specialty.name)
            except EOFError:
                break
    return list(dict.fromkeys(specialty_list))


def read_students_information() -> list[Student]:
    list_of_students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                list_of_students.append(pickle.load(pickle_file))
            except EOFError:
                break
    return list_of_students
