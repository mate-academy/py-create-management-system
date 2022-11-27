from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open("groups.pickle", "wb") as fs_groups:
        pickle.dump(groups, fs_groups)
    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as fs_students:
        pickle.dump(students, fs_students)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as fs_groups:
        groups = pickle.load(fs_groups)
    return sorted(set([group.specialty.name for group in groups]))


def read_students_information() -> list[str]:
    with open("students.pickle", "rb") as fs_students:
        students = pickle.load(fs_students)
    return students
