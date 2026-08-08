from dataclasses import dataclass
from datetime import datetime
from typing import List
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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as group:
        pickle.dump(groups, group)
    number_student = []
    for group in groups:
        number_student.append((len(group.students)))
    return max(number_student) if number_student else number_student


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as g:
        groups = pickle.load(g)
    name_ls = []
    for group in groups:
        if group.specialty.name not in name_ls:
            name_ls.append(group.specialty.name)
    return name_ls


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as student_ls:
        pickle.dump(students, student_ls)
    return len(students)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as s:
        return pickle.load(s)
