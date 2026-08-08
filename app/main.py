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
    course: int
    students: List[Student]


def write_groups_information(groups: list):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    students_list = []
    for group in groups:
        students_list.append(len(group.students))
    if students_list:
        return max(students_list)


def write_students_information(students: list):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
        return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        users = pickle.load(file)
    res = []
    for specialty in users:
        res.append(specialty.specialty.name)
    return set(res)


def read_students_information():
    with open("students.pickle", "rb") as file:
        user = pickle.load(file)
        return user
