from dataclasses import dataclass
from datetime import datetime
from typing import List
import pickle


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


def write_groups_information(groups: List[Group]) -> int | list:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    if len(groups) > 0:
        return max([len(group.students) for group in groups])
    return []


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> List[Group]:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return [student for student in students]
