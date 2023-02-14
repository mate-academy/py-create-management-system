from __future__ import annotations
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


def write_groups_information(list_of_group: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_in:
        pickle.dump(list_of_group, file_in)
    result = []
    for group in list_of_group:
        for student in group.students:
            if student not in result:
                result.append(student)
    return len(result)


def write_students_information(list_of_student: List[Student]) -> int:
    with open("students.pickle", "wb") as file_in:
        pickle.dump(list_of_student, file_in)
    return len(list_of_student)


def read_groups_information() -> List[Group]:
    with open("groups.pickle", "rb") as file_out:
        list_of_group = pickle.load(file_out)
    result = set([spec.specialty.name for spec in list_of_group])
    return list(result)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_out:
        list_of_students = pickle.load(file_out)
    return list_of_students
