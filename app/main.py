from dataclasses import dataclass
from typing import List
import pickle


@dataclass
class Speciality:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    speciality: Speciality
    course: int
    students: List[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups, pickle_groups)
    group_dict = {group.speciality.name: len(group.students) for group in groups}
    students_number = 0
    for key, value in group_dict.items():
        students_number += value
    return students_number


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students, pickle_students)
    return len(students)


def read_groups_information(group_pickle: str) -> list:
    with open(group_pickle, "rb") as pickle_groups:
        groups = pickle.load(pickle_groups)

    return set([group.speciality.name for group in groups])


def read_student_information(students_pickle: str) -> list:
    with open(students_pickle, "rb") as pickle_students:
        students = pickle.load(pickle_students)

    return list(students)
