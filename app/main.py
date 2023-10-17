import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Speciality:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    second_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    adress: str


@dataclass
class Group:
    speciality: Speciality
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> List[str]:
    with open() as file:
        groups = pickle.loads(file)

    return list(set(group.specialty.name for group in groups))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
