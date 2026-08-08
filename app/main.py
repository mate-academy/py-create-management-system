import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List, Set


GROUP_FILE = "groups.pickle"
STUDENT_FILE = "students.pickle"


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
    max_count = 0
    for group in groups:
        max_count = max(max_count, len(group.students))
    with open(GROUP_FILE, "wb") as writer:
        pickle.dump(groups, writer)
    return max_count


def write_students_information(students: List[Student]) -> int:
    with open(STUDENT_FILE, "wb") as writer:
        pickle.dump(students, writer)
    return len(students)


def read_groups_information() -> Set[str]:
    groups = None
    with open(GROUP_FILE, "rb") as reader:
        groups = pickle.load(reader)
    group_names = set()
    for group in groups:
        group_names.add(group.specialty.name)
    return group_names


def read_students_information() -> List[Student]:
    students = []
    with open(STUDENT_FILE, "rb") as reader:
        students = pickle.load(reader)
    return students
