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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(groups_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups_list, pickle_groups)
    max_number_of_students = 0
    for group in groups_list:
        if len(group.students) > max_number_of_students:
            max_number_of_students = len(group.students)
    return max_number_of_students


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students_list, pickle_students)
    return len(students_list)


def read_groups_information() -> list:
    result_list = []
    with open("groups.pickle", "rb") as pickle_groups:
        the_list_of_groups = pickle.load(pickle_groups)
        for group in the_list_of_groups:
            if group.specialty.name not in result_list:
                result_list.append(group.specialty.name)
    return result_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_students:
        list_of_students = pickle.load(pickle_students)
    return list_of_students
