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
    students_in_groups = []
    with open("groups.pickle", "wb") as group_file:
        for group in group_list:
            pickle.dump(group, group_file)
            for person in group.students:
                if person not in students_in_groups:
                    students_in_groups.append(person)
    return len(students_in_groups)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students_list:
            pickle.dump(student, students_file)
    return len(students_list)


def read_groups_information() -> list:
    spec_names = []
    with open("groups.pickle", "rb") as group_file:
        try:
            while True:
                spec_names.append(pickle.load(group_file).specialty.name)
        except EOFError:
            pass
    return list(set(spec_names))


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as students_file:
        try:
            while True:
                students_list.append(pickle.load(students_file))
        except EOFError:
            pass
    return students_list
