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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups_info, pickle_file)
    if len(groups_info) != 0:
        return max([len(group.students) for group in groups_info])


def write_students_information(students_info: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students_info, pickle_file)
    return len(students_info)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        groups_info = pickle.load(pickle_file)
    specialties = {group.specialty.name for group in groups_info}
    return specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students_info = pickle.load(pickle_file)
    return students_info
