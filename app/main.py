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
    birth_date: datetime
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
    with open("groups.pickle", "wb") as target:
        pickle.dump(groups, target)

    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as target:
        pickle.dump(students, target)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as target:
        groups = pickle.load(target)
        groups = [group.specialty.name for group in groups]
        return set(groups)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as target:
        return pickle.load(target)
