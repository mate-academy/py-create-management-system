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


def write_groups_information(groups_list: list) -> int:
    max_number_stud = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups_list:
            if max_number_stud < len(group.students):
                max_number_stud = len(group.students)
            pickle.dump(group, pickle_file)
    return max_number_stud


def write_students_information(students_list: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students_list:
            pickle.dump(student, pickle_file)
    return len(students_list)


def read_groups_information() -> list:
    group_list = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group_list.append(pickle.load(pickle_file).specialty.name)
            except EOFError:
                break
    return list(set(group_list))


def read_students_information() -> list:
    stud_list = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                stud_list.append(pickle.load(pickle_file))
            except EOFError:
                break
    return stud_list
