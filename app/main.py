import pickle
from datetime import datetime
from dataclasses import dataclass


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
    students: list


def write_groups_information(groups: list) -> int:
    people = 0
    with open("groups.pickle", "wb") as f:
        for item in groups:
            pickle.dump(item, f)
            if len(item.students) > people:
                people = len(item.students)
    return people


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as k:
        for items in students:
            pickle.dump(items, k)
    return len(students)


def read_groups_information() -> list:
    tech = []
    with open("groups.pickle", "rb") as j:
        while True:
            try:
                group = pickle.load(j)
                if group.specialty.name not in tech:
                    tech.append(group.specialty.name)
            except EOFError:
                break
    return tech


def read_students_information() -> list:
    new_tech = []
    with open("students.pickle", "rb") as i:
        while True:
            try:
                students = pickle.load(i)
                new_tech.append(students)
            except EOFError:
                break
    return new_tech
