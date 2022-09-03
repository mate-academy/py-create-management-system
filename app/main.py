import dataclasses
import pickle
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(group_list):
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)
    students_count = [len(group.students) for group in group_list]
    if len(students_count) != 0:
        return max(students_count)


def write_students_information(students_list):
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        return list(set(group.specialty.name for group in pickle.load(file)))


def read_students_information():
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
