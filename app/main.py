import dataclasses
from datetime import datetime
from typing import List
import pickle


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: int
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: list) -> int:
    with open("groups.pickle", "wb") as group_file:
        for group in group_list:
            pickle.dump(group, group_file)

    the_biggest_group = 0
    for group in group_list:
        length = len(group.students)
        if length > the_biggest_group:
            the_biggest_group = length
    return the_biggest_group


def write_students_information(student_list: list) -> int:

    how_students = len(student_list)
    with open("students.pickle", "wb") as student_file:
        for student in student_list:
            pickle.dump(student, student_file)
    return how_students


def read_groups_information() -> list:
    specialities = []
    with open("groups.pickle", "rb") as group_file_pickle:
        while True:
            try:
                group = pickle.load(group_file_pickle)
                speciality = group.specialty.name
                if speciality not in specialities:
                    specialities.append(speciality)
            except EOFError:
                break
    return specialities


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as student_file_pickle:
        while True:
            try:
                student = pickle.load(student_file_pickle)
                students.append(student)
            except EOFError:
                break
    return students
