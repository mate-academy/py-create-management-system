from dataclasses import dataclass
from datetime import datetime
import pickle


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_group:
        pickle.dump(groups, file_group)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_student:
        pickle.dump(students, file_student)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)
        specialities = []
        for group in groups:
            if group.specialty.name not in specialities:
                specialities.append(group.specialty.name)
        return specialities


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
