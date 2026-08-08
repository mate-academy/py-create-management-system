import dataclasses
import pickle
from datetime import date
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open("groups.pickle", "wb") as group_pickle:
        pickle.dump(group_list, group_pickle)
    return max(map(len, [group.students for group in group_list]), default=0)


def write_students_information(student_list: List[Student]) -> int:
    with open("students.pickle", "wb") as student_picle:
        pickle.dump(student_list, student_picle)
    return len(student_list)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as group_pickle:
        groups = pickle.load(group_pickle)
    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as group_pickle:
        student_list = pickle.load(group_pickle)
    return student_list
