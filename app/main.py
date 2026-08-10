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
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
        pickle.dump(groups, f)
    return max_students


def write_students_information(students: list[Student]) -> int:
    students_num = 0
    with open("students.pickle", "wb") as f:
        for student in students:
            students_num += 1
        pickle.dump(students, f)
    return students_num


def read_groups_information() -> set:
    specialties = []
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        for group in groups:
            specialties.append(group.specialty.name)
    return set(specialties)


def read_students_information() -> list[Student]:
    students_list = []
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        for student in students:
            students_list.append(student)
    return students_list
