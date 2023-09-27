import dataclasses
import pickle
from datetime import datetime
from typing import List, Any


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students_num = []
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    for unit in groups:
        max_students_num.append(len(unit.students))

    return max(max_students_num)


def write_students_information(pupil: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(pupil, file)

    return len(pupil)


def read_groups_information() -> List[Any]:
    with open("groups.pickle", "rb") as file:
        all_groups = pickle.load(file)

    specialty_names = list(set(group.specialty.name for group in all_groups))

    return specialty_names


def read_students_information() -> List:
    with open("students.pickle", "rb") as file:
        all_students = pickle.load(file)

    return all_students
