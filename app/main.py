import pickle
from typing import List
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            student_length = len(group.students)
            if max_students < student_length:
                max_students = student_length

    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> set:
    specialities = set()

    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:
                group = pickle.load(groups_file)
                specialities.add(group.specialty.name)
            except EOFError:
                break

    return specialities


def read_students_information() -> List[Student]:
    students = []

    with open("students.pickle", "rb") as students_file:
        while True:
            try:
                student = pickle.load(students_file)
                students.append(student)
            except EOFError:
                break

    return students
