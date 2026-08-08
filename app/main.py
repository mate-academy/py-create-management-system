from dataclasses import dataclass
from datetime import date
from typing import List
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
    students: list


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if groups:
        return max([len(st.students) for st in groups])

    return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        group = pickle.load(f)

    courses = {i.specialty.name for i in group}
    return [course for course in courses]


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        data = pickle.load(f)

    return data
