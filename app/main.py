from dataclasses import dataclass
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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(list_of_groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in list_of_groups:
            pickle.dump(group, pickle_file)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in list_of_students:
            pickle.dump(student, pickle_file)
    return len(list_of_students)


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


def read_students_information() -> List[Student]:
    students_list = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students_list.append(student)
            except EOFError:
                break
    return students_list
