import pickle
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


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
    students: List[Student] = field(default_factory=list)


def find_max_students(groups):
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_groups_information(groups):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students_count = find_max_students(groups)
    return max_students_count


def write_students_information(students):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = set(group.specialty.name for group in groups)
    return list(specialties)


def read_students_information():
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
