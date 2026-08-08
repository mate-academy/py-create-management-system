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
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    students_list = []
    for group in group_list:
        students_list.append(len(group.students))
    return max(students_list) if students_list else []


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)
    return len(list_of_students)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        specialty_names = [group.specialty.name for group in pickle.load(f)]
    return set(specialty_names)


def read_students_information():
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)
    return students_list
