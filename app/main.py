import pickle
import dataclasses
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
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)
    return max(len(group.students) for group in groups) if groups else []


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
    return list(set(group.specialty.name for group in groups))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as group_file:
        students = pickle.load(group_file)
    return students
