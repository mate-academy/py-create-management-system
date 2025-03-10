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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Student
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students: int = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        group_ = pickle.load(f)
    for group in group_:
        specialties.add(group.specialty.name)
    return specialties


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as f:
        student_info = pickle.load(f)
    for student in student_info:
        students_list.append(student)
    return students_list
