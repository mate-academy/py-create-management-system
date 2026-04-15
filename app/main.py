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


def write_groups_information(groups_list: list[Group]) -> int | None:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups_list, pickle_file)
    if groups_list:
        return max(len(group.students) for group in groups_list)
    return None


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students_list, pickle_file)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        groups_list = pickle.load(pickle_file)
    return set(group.specialty.name for group in groups_list)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students_list = pickle.load(pickle_file)
    return students_list
