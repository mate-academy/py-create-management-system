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
    birth_date: datetime.date
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
    max_students = 0

    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as file:
        groups_data = pickle.load(file)

    group_specialties = set()
    for group in groups_data:
        group_specialties.add(group.specialty.name)

    return group_specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students_data = pickle.load(file)
    return students_data
