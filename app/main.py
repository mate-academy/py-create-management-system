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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if len(groups) == 0:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)

    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    groups_specialty = [group.specialty.name for group in groups]
    return set(groups_specialty)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
