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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)
        if len(list_of_groups) == 0:
            return 0
    return max([len(x.students) for x in list_of_groups])


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)
    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
