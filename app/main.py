from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int | str
    students: list[Student]


def write_groups_information(lst_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(lst_of_groups, pickle_file)
    number_of_students = 0
    for group in lst_of_groups:
        if number_of_students < len(group.students):
            number_of_students = len(group.students)
    return number_of_students


def write_students_information(lst_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in lst_of_students:
            pickle.dump(student, pickle_file)
    return len(lst_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        lst_of_groups = pickle.load(pickle_file)
    lst_of_specialties = []
    for group in lst_of_groups:
        lst_of_specialties.append(group.specialty.name)
    return set(lst_of_specialties)


def read_students_information() -> list:
    lst_of_students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                lst_of_students.append(student)
            except EOFError:
                break
    return lst_of_students
