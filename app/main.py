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
    result = 0
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    for group in groups:
        if len(group.students) > result:
            result = len(group.students)

    return result


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
