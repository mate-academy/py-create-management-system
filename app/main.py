import pickle
from dataclasses import dataclass
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group, f)
    max_group = 0
    for i in group:
        if len(i.students) > max_group:
            max_group = len(i.students)
    return max_group


def write_students_information(student: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(student, f)
    return len(student)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    return set(group.specialty.name for group in groups)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
