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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    if not all(isinstance(group, Group) for group in groups):
        raise ValueError("Expected a list of Group instances.")

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    if not all(isinstance(student, Student) for student in students):
        raise ValueError("Expected a list of Student instances.")

    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> List[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
        if not isinstance(groups, list) or not all(isinstance(group, Group) for group in groups):
            raise ValueError("Invalid data format in groups.pickle")
        return list(set(group.specialty.name for group in groups))
    except (FileNotFoundError, EOFError, ValueError):
        return []


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
        if not isinstance(students, list) or not all(isinstance(student, Student) for student in students):
            raise ValueError("Invalid data format in students.pickle")
        return students
    except (FileNotFoundError, EOFError, ValueError):
        return []


