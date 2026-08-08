from dataclasses import dataclass
from datetime import datetime
from typing import List, Set
import pickle


GROUPS_DATA = "groups.pickle"
STUDENTS_DATA = "students.pickle"


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


def write_groups_information(groups: List[Group]) -> int:
    largest_group = 0

    with open(GROUPS_DATA, "wb") as groups_data:
        for group in groups:
            largest_group = max(largest_group, len(group.students))
            pickle.dump(group, groups_data)

    return largest_group


def write_students_information(students: List[Student]) -> int:
    with open(STUDENTS_DATA, "wb") as students_data:
        for student in students:
            pickle.dump(student, students_data)

    return len(students)


def read_groups_information() -> Set[str]:
    groups = []
    with open(GROUPS_DATA, "rb") as groups_data:
        while True:
            try:
                groups.append(pickle.load(groups_data))
            except EOFError:
                break

    return set([group.specialty.name for group in groups])


def read_students_information() -> List[Student]:
    students = []
    with open(STUDENTS_DATA, "rb") as students_data:
        while True:
            try:
                students.append(pickle.load(students_data))
            except EOFError:
                break

    return students
