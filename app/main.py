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
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)

    specialty_names = []

    for group in groups:
        if group.specialty.name not in specialty_names:
            specialty_names.append(group.specialty.name)

    return specialty_names


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)

    return students
