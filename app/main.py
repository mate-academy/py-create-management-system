from dataclasses import dataclass
from datetime import date
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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if groups:
        return max(len(group.students) for group in groups)


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(student_list, pickle_file)
    return len(student_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        group_list = pickle.load(pickle_file)
    if group_list:
        return list(set([group.specialty.name for group in group_list]))
    return []


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        student_list = pickle.load(pickle_file)
    return student_list
