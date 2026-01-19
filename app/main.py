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
    birth_date: datetime.date
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

    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)

    max_len = 0

    for group in groups:
        if max_len < len(group.students):
            max_len = len(group.students)
    return max_len


def write_students_information(
        students: list[Student]
) -> int:

    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> list[Specialty]:

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:

    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
