from dataclasses import dataclass
from datetime import date
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
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0
    return max([len(i.students) for i in groups])


def write_students_information(users):
    with open("students.pickle", "wb") as f:
        pickle.dump(users, f)
    return len(users)


def read_groups_information():
    with open("groups.pickle", "rb") as r:
        group_list = pickle.load(r)
        return set([i.specialty.name for i in group_list])


def read_students_information():
    with open("students.pickle", "rb") as r:
        return pickle.load(r)
