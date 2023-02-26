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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_ls: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_info:
        pickle.dump(group_ls, group_info)

    return max([len(group.students) for group in group_ls]) \
        if len(group_ls) > 0 else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_info:
        pickle.dump(students, student_info)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as read_info:
        groups = pickle.load(read_info)
    speciality_list = []
    for group in groups:
        speciality_list.append(group.specialty.name)
    return set(speciality_list)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as read_info:
        students = pickle.load(read_info)
    return students

