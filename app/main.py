import dataclasses
from datetime import datetime
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if groups:
        return max(len(group.students) for group in groups)

    return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list:
    set_specialty = set()

    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    for group in groups:
        set_specialty.add(group.specialty.name)

    return list(set_specialty)


def read_students_information() -> list:
    student_list = []

    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    for student in students:
        student_list.append(student)

    return student_list
