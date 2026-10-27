from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: str


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(lst: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(lst, pickle_file)
    return max((len(group.students) for group in lst), default=0)


def write_students_information(lst: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_fil:
        pickle.dump(lst, pickle_fil)
    return len(lst)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as pickle_fi:
        groups = pickle.load(pickle_fi)

    return {group.specialty.name for group in groups}


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_f:
        groups = pickle.load(pickle_f)
    return groups
