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
    birth_date: datetime.now()
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int | list:
    with open("groups.pickle", "wb") as group_file:
        for group in group_list:
            pickle.dump(group, group_file)
    if group_list:
        return max([len(group.students) for group in group_list])
    return []


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in student_list:
            pickle.dump(student, student_file)
    return len(student_list)


def read_groups_information() -> list[str]:
    groups = []
    with open("groups.pickle", "rb") as group_pickle:
        while True:
            try:
                groups.append(pickle.load(group_pickle))
            except EOFError:
                break
    groups_specialties = []
    for group in groups:
        if group.specialty.name not in groups_specialties:
            groups_specialties.append(group.specialty.name)
    return groups_specialties


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as student_pickle:
        while True:
            try:
                students.append(pickle.load(student_pickle))
            except EOFError:
                break
    return [student for student in students]
