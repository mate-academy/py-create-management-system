import dataclasses
from datetime import datetime
from typing import List
import pickle


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
    with open("groups.pickle", "wb") as file_obj:
        pickle.dump(groups, file_obj)

    if len(groups) == 0:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_obj:
        pickle.dump(students, file_obj)
    return len(students)


def read_groups_information() -> List:
    with open("groups.pickle", "rb") as file_obj:
        groups = pickle.load(file_obj)
        specialty = list(set([group.specialty.name for group in groups]))
    return specialty


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_obj:
        students = pickle.load(file_obj)
    return students
