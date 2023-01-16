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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> List[Specialty]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    result = []
    for group in groups:
        if group.specialty.name not in result:
            result.append(group.specialty.name)
    return result


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
