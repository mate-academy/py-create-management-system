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
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    return 0 if groups == [] else max(
        len(group.students) for group in groups if groups != []
    )


def write_students_information(students: list[Student]) -> int:
    all_students = len(students)
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return all_students


def read_groups_information() -> list:
    groups_list = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

    for group in groups:
        groups_list.append(group.specialty.name)

    return [] if groups == [] else list(set(groups_list))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)

    return students
