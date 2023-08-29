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
    phone_number: int
    address: int


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as report:
        pickle.dump(groups, report)
    return max([len(group.students) for group in groups]) if groups else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as report:
        pickle.dump(students, report)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as report:
        data = pickle.load(report)
    specialties = set(group.specialty.name for group in data)
    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as report:
        students = pickle.load(report)
    return students
