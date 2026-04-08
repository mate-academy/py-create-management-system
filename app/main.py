import dataclasses
from datetime import datetime
import pickle


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
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    ls = []
    for group in groups:
        ls.append(len(group.students))
    return max(ls, default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as groups_file:
        pickle.dump(students, groups_file)
    return len(students)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return students


def read_groups_information() -> set[str]:
    specialty_ls = []
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
    for group in groups:
        specialty_ls.append(group.specialty.name)
    return set(specialty_ls)
