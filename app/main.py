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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)
    return max((len(group.students) for group in list_of_groups), default=0)


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)
    return len(list_of_students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        list_of_groups = pickle.load(f)
    return list(set((group.specialty.name for group in list_of_groups)))


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        list_of_students = pickle.load(f)
    return list_of_students
