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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_json:
        pickle.dump(groups, groups_json)
    groups_students_len = [len(group.students) for group in groups]

    return max(groups_students_len) if groups_students_len else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_json:
        pickle.dump(students, students_json)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_json:
        groups = pickle.load(groups_json)

    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_json:
        students = pickle.load(students_json)

    return [student for student in students]
