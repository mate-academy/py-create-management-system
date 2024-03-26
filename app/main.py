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
    birth_date: datetime.date
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
    max_quantity = 0
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
        for group in groups:
            if max_quantity < len(group.students):
                max_quantity = len(group.students)
    return max_quantity


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    output = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        for group in groups:
            output.append(group.specialty.name)
    return list(set(output))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        output = pickle.load(pickle_file)
    return output
