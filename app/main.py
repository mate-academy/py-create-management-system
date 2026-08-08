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


def write_groups_information(group_instances: list[Group]) -> int:
    numbers_of_students = [
        len(group.students)
        for group in group_instances
    ]
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(group_instances, groups_file)
    return max(numbers_of_students) if numbers_of_students else 0


def write_students_information(student_instances: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(student_instances, students_file)
    return len(student_instances)


def read_groups_information() -> set:
    groups = []
    with open("groups.pickle", "rb") as groups_file:
        for group in pickle.load(groups_file):
            groups.append(group.specialty.name)
    return set(groups)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as students_file:
        for student in pickle.load(students_file):
            students.append(student)
    return students
