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
    students: list[Student]


GROUPS_FILE_NAME = "groups.pickle"
STUDENTS_FILE_NAME = "students.pickle"


def write_groups_information(groups: list[Group]) -> int:
    with open(GROUPS_FILE_NAME, "wb") as groups_file:
        pickle.dump(groups, groups_file)

    return max([len(group.students) for group in groups] or [0])


def write_students_information(students: list[Student]) -> int:
    with open(STUDENTS_FILE_NAME, "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information() -> set[str]:
    with open(GROUPS_FILE_NAME, "rb") as groups_file:
        groups: list[Group] = pickle.load(groups_file)

        return {group.specialty.name for group in groups}


def read_students_information() -> list[Student]:
    with open(STUDENTS_FILE_NAME, "rb") as students_file:
        return pickle.load(students_file)
