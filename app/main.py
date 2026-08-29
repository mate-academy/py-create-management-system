from dataclasses import dataclass
from datetime import date
from typing import List, Set
import pickle

GROUPS_FILE = "groups.pickle"
STUDENTS_FILE = "students.pickle"


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open(GROUPS_FILE, "wb") as file:
        pickle.dump(groups, file)

    max_students = max((len(group.students) for group in groups), default=0)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open(STUDENTS_FILE, "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> Set[str]:
    with open(GROUPS_FILE, "rb") as file:
        groups = pickle.load(file)

    specialties = {group.specialty.name for group in groups}
    return specialties


def read_students_information() -> List[Student]:
    with open(STUDENTS_FILE, "rb") as file:
        students = pickle.load(file)

    return students
