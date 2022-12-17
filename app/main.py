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
    birth_date: datetime
    average_mark: int
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_of_group: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups:
        pickle.dump(list_of_group, groups)
    return max([len(group.students) for group in list_of_group], default=0)


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as students:
        pickle.dump(list_of_students, students)
    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups:
        list_of_group = pickle.load(groups)
    return set([group.specialty.name for group in list_of_group])


def read_students_information() -> list:
    with open("students.pickle", "rb") as students:
        list_of_student = pickle.load(students)
    return list_of_student
