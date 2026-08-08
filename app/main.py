import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_list, f)
    return max((len(group.students) for group in groups_list)) \
        if groups_list else 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups_list = pickle.load(f)
        for group in groups_list:
            group.specialty.name
    return set(group.specialty.name for group in groups_list)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)
    return students_list
