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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_info: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file_group:
        pickle.dump(group_info, pickle_file_group)
        return (
            []
            if group_info == []
            else max([len(group.students) for group in group_info])
        )


def write_students_information(student_info: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file_students:
        pickle.dump(student_info, pickle_file_students)
    return len(student_info)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file_group:
        groups = pickle.load(pickle_file_group)
        return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file_students:
        return pickle.load(pickle_file_students)
