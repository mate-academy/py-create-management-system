from dataclasses import dataclass
from datetime import datetime
import pickle


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
    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    number_of_students = len(students)

    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return number_of_students


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        specialty_name = set([group.specialty.name for group in groups])

    return list(specialty_name)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
