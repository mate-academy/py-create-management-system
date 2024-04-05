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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_pickle:
        pickle.dump(groups, groups_pickle)
    return max(
        map(
            lambda group: len(group.students), groups
        )
    ) if groups else groups


def write_students_information(students: list[Group]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students, students_pickle)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_pickle:
        groups = pickle.load(groups_pickle)
    return list(set(map(lambda group: group.specialty.name, groups)))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_pickle:
        students = pickle.load(students_pickle)
    return students
