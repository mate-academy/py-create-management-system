import dataclasses
import pickle
from datetime import date
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: List[Specialty]
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_groups:
        pickle.dump(groups, file_groups)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_student:
        pickle.dump(students, file_student)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_groups:
        groups = pickle.load(file_groups)
    return list(
        set(
            [group.specialty.name for group in groups if group.specialty.name]
        )
    )


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_student:
        students = pickle.load(file_student)
    return students
