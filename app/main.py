import dataclasses
import pickle
from datetime import datetime
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    count_of_students = []
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            count_of_students.append(len(group.students))
            pickle.dump(group, pickle_file)
    return max(count_of_students) if count_of_students else 0


def write_students_information(student_list: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_list:
            pickle.dump(student, pickle_file)
    return len(student_list)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return specialties


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                students.append(pickle.load(pickle_file))
            except EOFError:
                break
    return students
