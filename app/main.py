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
    students: list


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    amount_of_students = []
    if not groups:
        return 0
    for group in groups:
        amount_of_students.append(len(group.students))
    return max(amount_of_students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    amount_of_groups = []
    for group in groups:
        amount_of_groups.append(group.specialty.name)
    return set(amount_of_groups)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
