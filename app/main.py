import dataclasses
from datetime import datetime
import pickle
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_out:
        pickle.dump(groups, file_out)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_out:
        pickle.dump(students, file_out)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)
        specialties = [group.specialty.name for group in groups]
        return sorted(set(specialties))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
