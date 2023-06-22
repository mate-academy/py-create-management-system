import dataclasses
import pickle
from datetime import date
from typing import List


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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    count_students = 0
    for count in groups:
        if len(count.students) > count_students:
            count_students = len(count.students)

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return count_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    specialties = []
    with open("groups.pickle", "rb") as file:
        data: List[Group] = pickle.load(file)
        for group in data:
            if group.specialty.name not in specialties:
                specialties.append(group.specialty.name)
    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        data: List[Student] = pickle.load(file)
    return data
