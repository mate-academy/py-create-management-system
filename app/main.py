from dataclasses import dataclass
from datetime import datetime
from pickle import load, dump


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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        dump(list_of_groups, f)
    try:
        return max([len(group.students) for group in list_of_groups])
    except ValueError:
        return 0


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        dump(list_of_students, f)
    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        specialties_names = {group.specialty.name for group in load(f)}
    return specialties_names


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        list_of_students = load(f)
    return list_of_students
