from dataclasses import dataclass

from datetime import date

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
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        count_students = []
        for group in groups:
            pickle.dump(group, pickle_groups)
            count_students.append(len(group.students))
        if count_students:
            return max(count_students)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        for student in students:
            pickle.dump(student, pickle_students)
        return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_groups:
        groups = []
        try:
            while True:
                group = pickle.load(pickle_groups)
                groups.append(group.specialty.name)
        except EOFError:
            pass

        return list(set(groups))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as pickle_students:
        students = []
        try:
            while True:
                student = pickle.load(pickle_students)
                students.append(student)
        except EOFError:
            pass

        return students
