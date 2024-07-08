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
    with open("groups.pickle", "wb") as groups_pickle:
        pickle.dump(groups, groups_pickle)

    return max(len(groups.students) for groups in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students, students_pickle)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_pickle:
        groups = pickle.load(groups_pickle)

    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_pickle:
        students = pickle.load(students_pickle)

    return students
