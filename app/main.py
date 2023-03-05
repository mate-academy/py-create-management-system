import dataclasses
import pickle

from datetime import datetime
from typing import List


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
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_groups:
        pickle.dump([i for i in group_list], file_groups)
    try:
        res = max([len(i.students) for i in group_list])
    except ValueError:
        res = []
    return res


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        pickle.dump([i for i in students_list], file_students)

    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_groups:
        groups = pickle.load(file_groups)
    return set(i.specialty.name for i in groups)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_groups:
        return pickle.load(file_groups)
