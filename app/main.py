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


def write_groups_information(groups_list: list[Group]) -> int:

    with open("groups.pickle", "wb") as groups:
        pickle.dump(groups_list, groups)

    return (
        max([len(group.students) for group in groups_list])
        if len(groups_list) > 0
        else 0
    )


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information() -> set:

    with open("groups.pickle", "rb") as groups:
        groups_info = pickle.load(groups)

    return set([group.specialty.name for group in groups_info])


def read_students_information() -> list[Student]:

    with open("students.pickle", "rb") as students_file:
        students_info = pickle.load(students_file)

    return students_info
