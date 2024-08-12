from dataclasses import dataclass
from datetime import datetime
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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_group:
        pickle.dump(groups, pickle_group)
    max_group = 0
    for group in groups:
        if len(group.students) > max_group:
            max_group = len(group.students)
    return max_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students, pickle_students)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups:
        names_group = pickle.load(groups)
        specialty_names = {group.specialty.name for group in names_group}
        return specialty_names


def read_students_information() -> list:
    with open("students.pickle", "rb") as all_students:
        all_st = pickle.load(all_students)
    return all_st
