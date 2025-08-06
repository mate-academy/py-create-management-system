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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_group:
        for group in groups:
            pickle.dump(group, pickle_group)
    return max([len(group.students) for group in groups])


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_student:
        for student in students:
            pickle.dump(student, pickle_student)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_group:
        groups = pickle.load(pickle_group)
        return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_student:
        return pickle.load(pickle_student)
