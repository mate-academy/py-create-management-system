from datetime import datetime
from typing import List

import dataclasses
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as information_list:
        pickle.dump(group_list, information_list)
    amount_students = 0
    for students_in_group in group_list:
        if len(students_in_group.students) > amount_students:
            amount_students += len(students_in_group.students)
    return amount_students


def write_students_information(list_students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_information:
        pickle.dump(list_students, students_information)
    return len(list_students)


def read_groups_information(file_groups_pickle: str = "groups.pickle") -> set:
    specialty_list = []
    with open(file_groups_pickle, "rb") as read_information:
        read_group_list = pickle.load(read_information)
    for group in read_group_list:
        specialty_list.append(group.specialty.name)
    return set(specialty_list)


def read_students_information(
        file_students_pickle: str = "students.pickle"
) -> list:
    with open(file_students_pickle, "rb") as information_of_students:
        return pickle.load(information_of_students)
