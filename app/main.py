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
    with open("groups.pickle", "wb") as groups_pickle:
        pickle.dump(groups, groups_pickle)

    return (
        max(len(group.students) for group in groups) if groups else 0
    )


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students, students_pickle)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as groups_pickle:
        groups = pickle.load(groups_pickle)
    specialty_names = list({group.specialty.name for group in groups})

    return specialty_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_pickle:
        students = pickle.load(students_pickle)

    return students
