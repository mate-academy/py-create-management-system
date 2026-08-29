import dataclasses
from datetime import date
from typing import List, Set
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    return max([len(g.students) for g in groups])


def write_students_information(student: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student, file)
    return len(student)


def read_groups_information() -> Set[str]:
    with open("groups.pickle", "rb") as file:
        result_group = pickle.load(file)
    return {group.specialty.name for group in result_group}


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        read_info = pickle.load(file)
    return read_info
