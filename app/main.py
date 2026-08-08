import dataclasses
import pickle
from datetime import datetime
from typing import List


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
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        return 0

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> List:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)

            return list(set(group.specialty.name for group in groups))
    except FileNotFoundError:
        return []


def read_students_information() -> List:
    try:
        with open("students.pickle", "rb") as file:
            student_data = pickle.load(file)

            return student_data
    except FileNotFoundError:
        return []
