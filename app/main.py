import dataclasses
from typing import List
from datetime import date
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: float
    students: List[Student]


def write_groups_information(list):
    with open("groups.pickle", "wb") as file:
        pickle.dump(list, file)
        for i in list:
            return len(i.students)


def write_students_information(list):
    with open("students.pickle", "wb") as file:
        pickle.dump(list, file)
    return len(list)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        s = []
        for Group in groups:
            s.append(Group.specialty.name)
    return set(s)


def read_students_information():
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
