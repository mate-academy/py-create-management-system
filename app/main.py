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

    max_students = 0

    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    with open("groups.pickle", "wb") as f:
        f.write(pickle.dumps(groups))

    return max_students


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as f:
        f.write(pickle.dumps(students))

    return len(students)


def read_groups_information() -> set:

    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    return set([group.specialty.name for group in groups])


def read_students_information() -> list[Student]:

    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
