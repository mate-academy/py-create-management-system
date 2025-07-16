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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[Group]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    unique_specialties = {group.specialty.name for group in groups}
    return list(unique_specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
