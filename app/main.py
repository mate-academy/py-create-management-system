from datetime import datetime

import dataclasses
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        for group in group_info:
            pickle.dump(group, groups_file)

    return_result = 0
    for group in group_info:
        if len(group.students) > return_result:
            return_result = len(group.students)

    return return_result


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in students_list:
            pickle.dump(student, student_file)

    return len(students_list)


def read_groups_information() -> set:
    groups_list = []
    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:
                groups_list.append(pickle.load(groups_file))
            except EOFError:
                break

    groups_specialties = [group.specialty.name for group in groups_list]

    return set(groups_specialties)


def read_students_information() -> list[Student]:
    student_list = []

    with open("students.pickle", "rb") as student_file:
        while True:
            try:
                student_list.append(pickle.load(student_file))
            except EOFError:
                break

    return student_list
