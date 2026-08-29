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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_groups, file)
    students_list = []
    if list_groups != []:
        for group in list_groups:
            students_list.append(len(group.students))
        return max(students_list)


def write_students_information(list_student: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_student, file)
    return len(list_student)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        list_group = pickle.load(file)
        speciality_list = []
        for group in list_group:
            speciality_list.append(group.specialty.name)
    return list(set(speciality_list))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        list_student = pickle.load(file)
    return list_student
