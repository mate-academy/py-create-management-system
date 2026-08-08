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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as result_file:
        for group in groups:
            pickle.dump(group, result_file)
    if not groups:
        return 0
    max_students_count = max(len(group.students) for group in groups)
    return max_students_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as source_file:
        groups = []
        while True:
            try:
                groups.append(pickle.load(source_file))
            except EOFError:
                break

        specialties = set()
        for group in groups:
            specialties.add(group.specialty.name)
        return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as source_file:
        students = []
        while True:
            try:
                students.append(pickle.load(source_file))
            except EOFError:
                break
        return students
