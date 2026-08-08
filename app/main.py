import pickle
from dataclasses import dataclass
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
    students: List[Student]


def write_groups_information(groups: List[Group]):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max([len(group.students) for group in groups] + [0])


def write_students_information(students: List[Student]):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    return list({group.specialty.name for group in groups})


def read_students_information():
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
