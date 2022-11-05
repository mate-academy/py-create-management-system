import datetime
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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
        max_students = 0
        for group in groups:
            if max_students < len(group.students):
                max_students = len(group.students)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
    return set(group.specialty.name for group in groups)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return [student for student in students]
