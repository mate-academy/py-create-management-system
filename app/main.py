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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if groups:
        return len(max(groups, key=lambda x: len(x.students)).students)
    return 0


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)

    return len(students_list)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
