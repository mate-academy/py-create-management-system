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
    specialty: str
    course: str
    students: list


def write_groups_information(groups_list: list[Group]) -> int:
    max_student_number = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups_list:
            pickle.dump(group, pickle_file)
            if max_student_number < len(group.students):
                max_student_number = len(group.students)
    return max_student_number


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students_list:
            pickle.dump(student, pickle_file)
    return len(students_list)


def read_groups_information() -> list:
    group_specialty = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                if group.specialty.name not in group_specialty:
                    group_specialty.append(group.specialty.name)
            except EOFError:
                return group_specialty
    return group_specialty


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students.append(student)
            except EOFError:
                return students
    return students
