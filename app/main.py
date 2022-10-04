from dataclasses import dataclass
from datetime import datetime
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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: datetime
    students: List[Student]


def write_groups_information(group_list: list):
    with open("groups.pickle", "wb") as groups:
        pickle.dump(group_list, groups)
    result = str(group_list).count("Student")
    if result > 1:
        result -= 1
    return result


def write_students_information(student_list):
    with open("students.pickle", "wb") as students:
        pickle.dump(student_list, students)
    result = str(student_list).count("Student")
    return result


def read_groups_information():
    with open("groups.pickle", "rb") as groups:
        data = pickle.load(groups)
    result = []
    for topic in data:
        result.append(topic.specialty.name)
    return set(result)


def read_students_information():
    with open("students.pickle", "rb") as students:
        result = pickle.load(students)
    return result
