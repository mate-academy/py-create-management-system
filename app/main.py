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


def write_groups_information(groups: list[Group]):
    student_number: int = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            if student_number < len(group.students):
                student_number = len(group.students)
            pickle.dump(group, pickle_file)
    return student_number

def write_students_information(students: list[Student]):
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)

def read_groups_information():
    groups = []
    with open("groups.pickle", "rb") as pickle_file:
        groups.append(pickle.load(pickle_file))

def read_students_information():
    students = []
    with open("students.pickle", "rb") as pickle_file:
        students.append(pickle.load(pickle_file))
    return students
