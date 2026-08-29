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
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in group_list:
            pickle.dump(group, f)
    return 0 if not group_list else max(
        [len(group.students) for group in group_list]
    )


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in student_list:
            pickle.dump(student, f)
    return len(student_list)


def read_groups_information() -> set:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                group = pickle.load(f)
                specialties.add(group.specialty.name)
    except EOFError:
        pass
    return specialties


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                student = pickle.load(f)
                students.append(student)
    except EOFError:
        pass
    return students
