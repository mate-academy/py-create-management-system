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


def write_groups_information(list_of_group: list[Group]) -> int:
    maximum_number = 0
    for group in list_of_group:
        if maximum_number < len(group.students):
            maximum_number = len(group.students)
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_group, file)
    return maximum_number


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "br") as file:
        groups = pickle.load(file)
    return {group.specialty.name for group in groups}


def read_students_information() -> list:
    with open("students.pickle", "br") as file:
        students = pickle.load(file)
    return students
