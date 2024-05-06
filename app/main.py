import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_pickle:
        pickle.dump(groups, group_pickle)

    max_student = max(len(group.students) for group in groups) if groups else 0
    return max_student


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_pickle:
        pickle.dump(students, student_pickle)

    return len(students)


def read_groups_information() -> str:
    with open("groups.pickle", "rb") as groups_pickle:
        groups = pickle.load(groups_pickle)

        return {group.specialty.name for group in groups}


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as student_pickle:
        students = pickle.load(student_pickle)
    return students
