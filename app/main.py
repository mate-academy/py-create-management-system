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


def write_groups_information(groups: list) -> int:
    max_students = max((len(group.students) for group in groups), default=0)

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max_students


def write_students_information(students: list) -> int:
    students_count = len(students)

    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return students_count


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        specialty = []
        for group in groups:
            name = group.specialty.name
            if name not in specialty:
                specialty.append(name)
    return specialty


def read_students_information() -> Student:
    with open("students.pickle", "rb") as f:
        students_information = pickle.load(f)
    return students_information
