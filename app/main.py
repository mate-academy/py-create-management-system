from dataclasses import dataclass
from datetime import date
import pickle


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
    with open("groups.pickle", "wb") as fobj:
        pickle.dump(groups, fobj)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as fobj:
        pickle.dump(students, fobj)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as fobj:
        groups: list[Group] = pickle.load(fobj)
    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as fobj:
        students: list[Student] = pickle.load(fobj)
    return students
