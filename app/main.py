import dataclasses
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
    birth_date: str
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
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[str]:
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
        specialties = [group.specialty.name for group in groups]
        specialties = list(set(specialties))
        return specialties
    except FileNotFoundError:
        return []


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
        return students
    except FileNotFoundError:
        return []
