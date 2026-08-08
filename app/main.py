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
    students: Student


def write_groups_information(group_list: list) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)
    if len(group_list) == 0:
        return 0
    return max([len(group.students) for group in group_list])


def write_students_information(student_list: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(student_list, pickle_file)
    return len(student_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        return set([user.specialty.name for user in pickle.load(pickle_file)])


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        return [student for student in pickle.load(pickle_file)]
