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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_of_groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_for_groups_info:
        for group in list_of_groups:
            pickle.dump(group, file_for_groups_info)
    if not list_of_groups:
        return 0
    return max([len(group.students) for group in list_of_groups])


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_for_students_info:
        for student in list_of_students:
            pickle.dump(student, file_for_students_info)
    return len(list_of_students)


def read_groups_information() -> list:
    list_of_specialty = []
    with open("groups.pickle", "rb") as file_for_groups_info:
        while True:
            try:
                group = pickle.load(file_for_groups_info)
                list_of_specialty.append(group.specialty.name)
            except EOFError:
                break
    return list(set(list_of_specialty))


def read_students_information() -> List[Student]:
    list_of_students = []
    with open("students.pickle", "rb") as file_for_students_info:
        while True:
            try:
                list_of_students.append(pickle.load(file_for_students_info))
            except EOFError:
                break
    return list_of_students
