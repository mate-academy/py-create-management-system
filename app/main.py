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


class Group:
    specialty: Specialty
    course: int
    students: list[Student]

    def __init__(self, specialty: Specialty,
                 course: int,
                 students: list[Student]) -> None:
        self.specialty = specialty
        self.course = course
        self.students = students


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list[str]:
    specialties = set()
    with open("groups.pickle", "rb") as pickle_file:
        try:
            while True:
                group = pickle.load(pickle_file)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return list(specialties)


def read_students_information() -> list[Student]:
    student_list = []
    with open("students.pickle", "rb") as pickle_file:
        try:
            while True:
                student = pickle.load(pickle_file)
                student_list.append(student)
        except EOFError:
            pass
    return student_list
