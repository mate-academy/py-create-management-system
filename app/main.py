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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    students_count = []
    for group in groups:
        students_count.append(len(group.students))
    return max(students_count) if students_count else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups_list = pickle.load(file)

    spec_names = [group.specialty.name for group in groups_list]
    return set(spec_names)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_list = pickle.load(file)
    return students_list