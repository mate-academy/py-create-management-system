import pickle
from datetime import date
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open("groups.pickle", "wb") as groups_dump:
        pickle.dump(groups, groups_dump)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_dump:
        pickle.dump(students, students_dump)

    return len(students)


def read_groups_information() -> set[Specialty]:
    with open("groups.pickle", "rb") as groups_dump:
        return set([
            group.specialty.name
            for group in pickle.load(groups_dump)
        ])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_dump:
        return [
            student
            for student in pickle.load(students_dump)
        ]
