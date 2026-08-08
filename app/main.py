from dataclasses import dataclass
import pickle
from datetime import datetime


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    number_of_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(list_of_groups, pickle_file)
    for group in list_of_groups:
        if number_of_students < len(group.students):
            number_of_students = len(group.students)
    return number_of_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as stud_pickle_file:
        pickle.dump(list_of_students, stud_pickle_file)
        for student in list_of_students:
            pickle.dump(student, stud_pickle_file)
    return len(list_of_students)


def read_groups_information() -> list[Specialty]:
    with open("groups.pickle", "rb") as reading_group_info_file:
        data_of_groups = pickle.load(reading_group_info_file)
        list_of_specialties = []
        for group in data_of_groups:
            if group.specialty.name not in list_of_specialties:
                list_of_specialties.append(group.specialty.name)
        return list_of_specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as reading_students_info_file:
        list_of_students = pickle.load(reading_students_info_file)
        return list_of_students
