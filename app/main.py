import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int | float


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


def write_groups_information(groups: list[Group]):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    qty_of_students = 0
    for group in groups:
        qty_of_students += len(group.students)
    return qty_of_students


def write_students_information(students: list[Student]):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        data = pickle.load(file)
        return set([group.specialty.name for group in data])


def read_students_information():
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
