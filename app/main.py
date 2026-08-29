import dataclasses
import pickle
from datetime import datetime


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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information(file_path: str) -> set:
    with open(file_path, "rb") as f:
        all_groups = pickle.load(f)
        specialties = set(group.specialty.name for group in all_groups)
        return specialties


def read_students_information(file_path: str) -> list[Student]:
    with open(file_path, "rb") as f:
        all_students = list(pickle.load(f))
        return all_students
