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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> None:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list[Student]) -> None:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        data = pickle.load(f)
    return {student.specialty.name for student in data}


def read_students_information() -> dict:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
