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
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
        length = []
        for group in groups:
            if group.students:
                length.append(len(group.students))
        if length:
            return max(length)
        return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
        return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        info = pickle.load(pickle_file)
        set_ = set()
        for group in info:
            set_.add(group.specialty.name)
        return list(set_)


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        info = pickle.load(pickle_file)
        return info
