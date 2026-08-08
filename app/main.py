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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_number_of_student = 0
    with open("groups.pickle", "wb") as datafile:
        for group in groups:
            pickle.dump(group, datafile)
            if len(group.students) > max_number_of_student:
                max_number_of_student = len(group.students)
    return max_number_of_student


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as datafile:
        for student in students:
            pickle.dump(student, datafile)
    return len(students)


def read_groups_information() -> list:
    specialties = []
    with open("groups.pickle", "rb") as datafile:
        while True:
            try:
                group = pickle.load(datafile)
            except EOFError:
                break
            specialties.append(group.specialty.name)
    return list(set(specialties))


def read_students_information() -> list:
    instances = []
    with open("students.pickle", "rb") as datafile:
        while True:
            try:
                student = pickle.load(datafile)
            except EOFError:
                break
            instances.append(student)
    return instances
