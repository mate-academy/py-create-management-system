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


def write_groups_information(info_group: List[Group]) -> int:
    with open("groups.pickle", "wb") as group:
        pickle.dump(info_group, group)
        max_students = 0
        for student in info_group:
            max_students = max(max_students, len(student.students))
        return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> List[Specialty]:
    with open("groups.pickle", "rb") as f:
        return list(set(group.specialty.name for group in pickle.load(f)))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        return [student for student in pickle.load(f)]
