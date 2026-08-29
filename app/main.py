import pickle
from dataclasses import dataclass
import datetime
from typing import List


@dataclass
class Specialty:
    name : str
    number : int


@dataclass
class Student:
    first_name : str
    last_name : str
    birth_date : datetime.date
    average_mark : float
    has_scholarship : bool
    phone_number : str
    address : str


@dataclass
class Group:
    specialty : Specialty
    course: int
    students : List[Student]


def write_groups_information(groups_list: List[Group]) -> int:
    result = []
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_list, file)
        for group in groups_list:
            result.append(len(group.students))
    if not result :
        return 0
    return max(result)


def write_students_information(students_list: List[Student]) -> int :
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> set:
    result = []
    with open("groups.pickle", "rb") as file:
        group_list = pickle.load(file)
        for group in group_list:
            result.append(group.specialty.name)
    return set(result)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students_list = pickle.load(file)
    return students_list
