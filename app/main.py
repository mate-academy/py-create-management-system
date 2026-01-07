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
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> List[str]:
    groups = []
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    groups.append(pickle.load(f))
                except EOFError:
                    break
    except (FileNotFoundError, EOFError):
        return []

    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    students.append(pickle.load(f))
                except EOFError:
                    break
    except (FileNotFoundError, EOFError):
        return []

    return students
