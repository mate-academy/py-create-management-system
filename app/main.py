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
    """

    :param groups:
    :return: This function returns the maximum number
    of students from all the groups.
    """
    with open("groups.pickle", "wb") as pickle_file:
        for user in groups:
            pickle.dump(user, pickle_file)

    students = [len(group.students) for group in groups]
    if students:
        max_students = max(students)
        return max_students
    return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)

    return len(students)


def read_groups_information() -> list[Specialty]:
    with open("groups.pickle", "rb") as file:
        groups = []
        while True:
            try:
                group = pickle.load(file)
                groups.append(group)
            except EOFError:
                break
        specialties = set(group.specialty.name for group in groups)
        return list(specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = []
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break
        return students
