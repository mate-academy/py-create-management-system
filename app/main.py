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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)

    maximum_number_of_students = 0
    for group in group_list:
        if len(group.students) > maximum_number_of_students:
            maximum_number_of_students = len(group.students)

    return maximum_number_of_students


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(student_list, f)

    return len(student_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        group_list = pickle.load(f)

    specialty_list = []
    for group in group_list:
        if group.specialty.name not in specialty_list:
            specialty_list.append(group.specialty.name)

    return specialty_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        student_list = pickle.load(f)

    return student_list
