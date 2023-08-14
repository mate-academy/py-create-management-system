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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups, pickle_groups)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students, pickle_students)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
        specialties = list({group.specialty.name for group in groups})
        return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        return pickle.load(students_file)
