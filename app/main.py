from dataclasses import dataclass
from datetime import datetime
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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_of_groups: List[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file_group:
        for group in list_of_groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
            pickle.dump(group, pickle_file_group)
    return max_students


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file_students:
        for student in list_of_students:
            pickle.dump(student, pickle_file_students)
    return len(list_of_students)


def read_groups_information() -> List[Specialty]:
    list_with_specialties = []
    with open("groups.pickle", "rb") as pickle_file_group:
        try:
            while True:
                group = pickle.load(pickle_file_group).__dict__
                speciality_of_group = group["specialty"].name
                if speciality_of_group not in list_with_specialties:
                    list_with_specialties.append(speciality_of_group)
        except EOFError:
            return list_with_specialties


def read_students_information() -> List[Student]:
    list_of_students = []
    with open("students.pickle", "rb") as pickle_file_students:
        try:
            while True:
                student = pickle.load(pickle_file_students)
                list_of_students.append(student)
        except EOFError:
            return list_of_students
