from dataclasses import dataclass
from datetime import datetime
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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]):
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    max_students_number = []
    for group in groups:
        max_students_number.append(len(group.students))

    if not max_students_number:
        return 0
    return max(max_students_number)


def write_students_information(students: List[Student]):
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    return list(
        {
            group.specialty.name
            for group in groups
        }
    )


def read_students_information():
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
