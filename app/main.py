from dataclasses import dataclass
from typing import List
from datetime import datetime
import pickle


@dataclass
class Speciality:
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
    speciality: Speciality
    course: dict
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
