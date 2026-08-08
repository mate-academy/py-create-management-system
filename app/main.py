from datetime import datetime
from dataclasses import dataclass
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(groups: List[Group]):
    with open("groups.pickle", "wb") as file_in:
        pickle.dump(groups, file_in)

    max_students = []

    for group in groups:
        max_students.append(len(group.students))
    return max(max_students) if max_students else 0


def write_students_information(students: List[Student]):
    with open("students.pickle", "wb") as file_in:
        pickle.dump(students, file_in)

    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)
        specialities = set()

        for group in groups:
            specialities.add(group.specialty.name)

    return list(specialities)


def read_students_information():
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
