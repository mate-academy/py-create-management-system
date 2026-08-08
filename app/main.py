# write your code here
from dataclasses import dataclass
import datetime
import pickle
from typing import List


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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if len(groups):
        return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        return list(
            set(group.specialty.name for group in pickle.load(pickle_file))
        )


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        return [student for student in pickle.load(pickle_file)]
