# write your code here
import dataclasses
from datetime import date
from typing import List
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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    maximum_number_of_students = 0

    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            if len(group.students) > maximum_number_of_students:
                maximum_number_of_students = len(group.students)
        pickle.dump(groups, pickle_file)

    return maximum_number_of_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> list:
    groups_specialties = []

    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

        for group in groups:
            if group.specialty.name not in groups_specialties:
                groups_specialties.append(group.specialty.name)

    return groups_specialties


def read_students_information() -> list:
    students_list = []

    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
        for student in students:
            students_list.append(student)

    return students
