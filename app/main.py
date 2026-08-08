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
    course: str
    students: list[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file_out:
        pickle.dump(groups, file_out)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file_out:
        pickle.dump(students, file_out)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)
    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
