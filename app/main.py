import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_pickle_file:
        pickle.dump(groups, groups_pickle_file)

    return len(
        max(
            groups, key=lambda group: len(group.students),
            default=Group(None, None, [])
        ).students
    )


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle_file:
        pickle.dump(students, students_pickle_file)

    return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as groups_pickle_file:
        groups = pickle.load(groups_pickle_file)
        return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_pickle_file:
        return pickle.load(students_pickle_file)
