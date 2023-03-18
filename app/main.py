import dataclasses
from datetime import datetime
import pickle
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: int
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
        for group in groups:
            return len(group.students)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as read_pickle:
        groups = pickle.load(read_pickle)
        for group in groups:
            specialties.add(group.specialty.name)
        return list(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as read_students:
        students = pickle.load(read_students)
        return students
