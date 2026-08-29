import pickle
from dataclasses import dataclass
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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_with_groups:
        for group in group_list:
            pickle.dump(group, file_with_groups)
    if group_list:
        max_students = max(len(group.students) for group in group_list)
        return max_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file_with_students:
        for student in students_list:
            pickle.dump(student, file_with_students)
    return len(students_list)


def read_groups_information() -> set[str]:
    names_speciality = set()

    with open("groups.pickle", "rb") as data_about_group:
        while True:
            try:
                one_group = pickle.load(data_about_group)
                names_speciality.add(one_group.specialty.name)
            except EOFError:
                break

        return names_speciality


def read_students_information() -> list[Student]:
    students = []

    with open("students.pickle", "rb") as data_about_students:
        while True:
            try:
                student = pickle.load(data_about_students)
                students.append(student)
            except EOFError:
                break

        return students
