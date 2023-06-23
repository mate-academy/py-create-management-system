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
    birth_date: datetime.date
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
    with open("groups.pickle", "wb") as group_info_file:
        pickle.dump(groups, group_info_file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_info_file:
        pickle.dump(students, students_info_file)
    return len(students)


def read_groups_information() -> List:
    with open("groups.pickle", "rb") as group_info_file:
        groups = pickle.load(group_info_file)
    return (list(set(group.specialty.name for group in groups))
            if groups else [])


def read_students_information() -> List:
    with open("students.pickle", "rb") as students_info_file:
        students = pickle.load(students_info_file)
    return students
