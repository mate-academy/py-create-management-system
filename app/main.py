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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)

    max_students = 0
    for group in groups:
        if max_students < len(group.students):
            max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)
    return len(students)


def read_groups_information() -> list:
    specialty_list = []
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
        for group in groups:
            specialty_list.append(group.specialty.name)
    return list(set(specialty_list))


def read_students_information() -> list[Student]:
    students_list = []
    with open("students.pickle", "rb") as student_file:
        students = pickle.load(student_file)
        for student in students:
            students_list.append(student)
    return students_list
