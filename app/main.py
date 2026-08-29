import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: str


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


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        for group in groups_list:
            pickle.dump(group, pickle_groups)

    len_students = 0
    for group in groups_list:
        if len(group.students) >= len_students:
            len_students = len(group.students)
    return len_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students_list, pickle_students)

    return len(students_list)


def read_groups_information() -> set[str]:
    groups_set = set()
    with open("groups.pickle", "rb") as read_groups:
        while True:
            try:
                groups = (pickle.load(read_groups))
                groups_set.add(groups.specialty.name)
            except EOFError:
                break

    return groups_set


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as read_students:
        students_list = pickle.load(read_students)

    return students_list
