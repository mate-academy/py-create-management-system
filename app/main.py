from dataclasses import dataclass
import pickle
from typing import Any


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
    course: int
    students: list[Student]


def write_groups_information(list_of_group: list[Group]) -> int:
    res = 0
    with open("groups.pickle", "wb") as f:
        for students in list_of_group:
            pickle.dump(students, f)
    for stud in list_of_group:
        if len(stud.students) > res:
            res = len(stud.students)
    return res


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for students in list_of_students:
            pickle.dump(students, f)
    return len(list_of_students)


def read_groups_information() -> Any:
    my_list = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                res = pickle.load(f)
                if res.specialty.name not in my_list:
                    my_list.append(res.specialty.name)
            except EOFError:
                break
    return my_list


def read_students_information() -> list:
    my_list = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                res = pickle.load(f)
                my_list.append(res)
            except EOFError:
                break
    return my_list
