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
    with open("groups.pickle", "wb") as groups_picle:
        pickle.dump(groups, groups_picle)

    return max([len(group.students) for group in groups] or [0])


def write_students_information(student: list[Student]) -> int:
    with open("students.pickle", "wb") as student_picle:
        pickle.dump(student, student_picle)

    return len(student)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        data: list[Group] = pickle.load(pickle_file)

    return {element.specialty.name for element in data}


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        data: list[Student] = pickle.load(pickle_file)

    return [student for student in data]
