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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int | datetime
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    count_students = 0
    students_list = []
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    for group in groups:
        for student in group.students:
            if student not in students_list:
                count_students += 1
                students_list.append(student)
    return count_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    all_specialty = []
    with open("groups.pickle", "rb") as file:
        date_groups = pickle.load(file)
    for group in date_groups:
        if group.specialty.name not in all_specialty:
            all_specialty.append(group.specialty.name)
    return all_specialty


def read_students_information() -> list:
    date_result = []
    with open("students.pickle", "rb") as file:
        date_students = pickle.load(file)
    for student in date_students:
        if isinstance(student, Student):
            date_result.append(student)
    return date_result
