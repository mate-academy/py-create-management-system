from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List
from typing import Union


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
    course: str
    students: List[Student]


def write_groups_information(groups: list) -> Union[int, list]:
    if not groups:
        return []
    students_in_groups = []
    for group in groups:
        counter = 0
        for _ in group.students:
            counter += 1
        students_in_groups.append(counter)
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    return max(students_in_groups)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as read_file:
            groups = pickle.load(read_file)
        return list(set([group.specialty.name for group in groups]))
    except FileNotFoundError:
        return []


def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as read_file:
            students = list(pickle.load(read_file))
        return students
    except FileNotFoundError:
        return []
