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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as group_pickle:
        for group in groups_list:
            pickle.dump(group, group_pickle)
    return (
        max([len(group.students) for group in groups_list])
        if groups_list != []
        else 0
    )


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        for student in students_list:
            pickle.dump(student, students_pickle)
    return len(students_list)


def read_groups_information() -> list:
    result = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                result.append(pickle.load(file).specialty.name)
            except EOFError:
                return list(set(result))


def read_students_information() -> List[Student]:
    result = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                result.append(pickle.load(file))
            except EOFError:
                return result
