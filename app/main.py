from dataclasses import dataclass
from datetime import datetime
from typing import List
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_out:
        pickle.dump(group_list, file_out)
    if len(group_list) == 0:
        return 0
    return max(map(lambda x: len(x.students), group_list))


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)
        return set(map(lambda x: x.specialty.name, groups))


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as file_out:
        pickle.dump(students_list, file_out)
    return len(students_list)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
